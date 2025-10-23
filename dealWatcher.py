"""
This file is part of Deal Watcher.

Deal Watcher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

Deal Watcher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Deal Watcher.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import time
import datetime
import requests
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from typing import Union

# --- CONSTANTES DE CONFIGURAÇÃO ---
DEALS_URL = "https://deal.brokers.mktlab.app/"
DEAL_CONTAINER_SELECTOR = ".grid-cols-1.gap-4.md\\:grid.md\\:m-4.sm\\:grid-cols-2.md\\:grid-cols-3.lg\\:grid-cols-4.md\\:p-4"
POLLING_INTERVAL_SECONDS = 120
WAIT_FOR_PAGE_LOAD_SECONDS = 10
WEBHOOK_URL= " " #Webhook que receberá um payload com as informações do deal capturado
CHROME_USER_DATA_DIR="/home/v4percus/.config/google-chrome" #Caminho da pasta que contém o profile do chrome que já está logado na conta google que será utilizado no Deal Broker.
CHROME_PROFILE_DIR="Default" #Nome do profile do chrome que já está logado na conta google que será utilizado no Deal Broker
CHROME_BINARY_LOCATION="/home/v4percus/Documentos/reps/deal-watcher/depens/chrome-linux64/chrome" # Caminho para o binário do chrome for testing (pode ser obtido em https://storage.googleapis.com/chrome-for-testing-public/141.0.7390.122/linux64/chrome-linux64.zip )
RUN_HEADLESS="false"

# --- CONFIGURAÇÃO DO MODO DE TESTE ---
SEND_TEST_WEBHOOK = False # Quando esta variável for verdadeira, a primeira iteração do programa vai analisar o arquivo fornecido na constante da próxima linha, e contanto que este esteja dentro padrão esperado, um webhook será engatilhado com as informações da pág.
TEST_MODE_FILE = "" # Forneça um arquivo html extraido de uma página do Deal Broker que contenha Deals disponiveis para reserva, e este será utilizado para notificar na primeira iteração do programa


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("deal_monitor.log"),
            logging.StreamHandler()
        ]
    )

def setup_driver() -> Union[webdriver.Chrome, None]:
    try:
        logging.info("Configurando o driver do Chrome...")
        ChromeDriverManager().install()
        opcoes = webdriver.ChromeOptions()
        
        user_data_dir = CHROME_USER_DATA_DIR
        profile_dir = CHROME_PROFILE_DIR
        binary_location = CHROME_BINARY_LOCATION

        if user_data_dir:
            opcoes.add_argument(f'--user-data-dir={user_data_dir}')
        if profile_dir:
            opcoes.add_argument(f'--profile-directory={profile_dir}')
        if binary_location:
            opcoes.binary_location = binary_location
        
        opcoes.add_argument('--no-sandbox')
        if RUN_HEADLESS == 'true':
            opcoes.add_argument('--headless')
            opcoes.add_argument('--disable-gpu')

        driver = webdriver.Chrome(service=Service(), options=opcoes)
        logging.info("Driver do Chrome configurado com sucesso.")
        return driver
    except WebDriverException as e:
        logging.error(f"Falha ao inicializar o driver do Chrome: {e}")
        return None

def fetch_deals(driver: webdriver.Chrome) -> Union[dict, None]:
    """
    Analisa a página ATUAL em busca de ofertas após uma espera fixa.
    """
    try:
        logging.info(f"Aguardando {WAIT_FOR_PAGE_LOAD_SECONDS} segundos para o conteúdo carregar...")
        time.sleep(WAIT_FOR_PAGE_LOAD_SECONDS)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        if "No momento não existem ofertas disponíveis" in soup.get_text():
            logging.info("Nenhuma oferta encontrada na página (mensagem explícita).")
            return {} 

        deal_card_container = soup.select_one(DEAL_CONTAINER_SELECTOR)
        if not deal_card_container:
            logging.warning("Contêiner de ofertas não encontrado após a espera. Tratando como 'zero ofertas'.")
            return {}

        all_deal_cards = deal_card_container.find_all("div", recursive=False)
        current_deals = {}

        for card in all_deal_cards:
            deal_name_tag = card.find("p", class_="text-base text-left text-foreground")
            if not deal_name_tag:
                continue
            
            deal_name = deal_name_tag.get_text(strip=True)

            # --- FUNÇÃO DE EXTRAÇÃO DE DADOS CORRIGIDA ---
            def get_detail_text(card_element, label_text):
                """
                Função mais robusta que ignora espaços em branco e busca pelo
                rótulo para encontrar o valor correspondente no parágrafo seguinte.
                """
                all_paragraphs = card_element.find_all("p")
                for i, p_tag in enumerate(all_paragraphs):
                    # Compara o texto limpo (sem espaços/quebras de linha)
                    if p_tag.get_text(strip=True) == label_text:
                        # Se encontrarmos o rótulo, o valor é o próximo parágrafo na lista
                        if i + 1 < len(all_paragraphs):
                            return all_paragraphs[i + 1].get_text(strip=True)
                return "N/A" # Se não encontrar, retorna N/A

            current_deals[deal_name] = {
                'reserve' : get_detail_text(card, "Reserva atual"),
                'locName': get_detail_text(card, "Localização"),
                'Segmento': get_detail_text(card, "Segmento"),
                'Faturamento': get_detail_text(card, "Faturamento"),
            }
        
        logging.info(f"{len(current_deals)} ofertas encontradas na página.")
        return current_deals

    except Exception as e:
        logging.error(f"Erro inesperado ao analisar a página: {e}")
        return None

def send_notification(deal_name: str, deal_details: dict, webhook_url: str):
    payload = {'dealName': deal_name, **deal_details}
    try:
        logging.info(f"Enviando notificação para a oferta: '{deal_name}'")
        response = requests.post(webhook_url, json=payload, timeout=15)
        response.raise_for_status()
        logging.info(f"Webhook para '{deal_name}' enviado com sucesso.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Falha ao enviar webhook para '{deal_name}': {e}")

def save_debug_file(page_source: str, deal_name: str):
    try:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        safe_deal_name = deal_name.replace('/', '_').replace('\\', '_')
        filename = f"debug_{date_str}_{safe_deal_name}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(page_source)
        logging.info(f"Arquivo de depuração salvo: {filename}")
    except IOError as e:
        logging.error(f"Não foi possível salvar o arquivo de depuração para '{deal_name}': {e}")

def main():
    """Função principal que orquestra o processo de monitoramento."""
    setup_logging()
    
    webhook_url = WEBHOOK_URL
    if not webhook_url:
        logging.critical("A URL do webhook não está definida. O script não pode continuar.")
        return

    driver = setup_driver()
    if not driver:
        return

    if SEND_TEST_WEBHOOK:
        logging.info("--- MODO DE TESTE DO WEBHOOK ATIVADO (ARQUIVO LOCAL) ---")
        try:
            file_path = os.path.abspath(TEST_MODE_FILE)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Arquivo de teste não encontrado: {file_path}")

            local_file_url = Path(file_path).as_uri()
            
            logging.info(f"Abrindo arquivo local: {local_file_url}")
            driver.get(local_file_url)

            deals_from_file = fetch_deals(driver)

            if deals_from_file:
                first_deal_name = list(deals_from_file.keys())[0]
                first_deal_details = deals_from_file[first_deal_name]

                logging.info(f"Encontrada oferta de teste no arquivo: '{first_deal_name}'")
                send_notification(first_deal_name, first_deal_details, webhook_url)
            else:
                logging.warning("Nenhuma oferta encontrada no arquivo de teste.")

        except (FileNotFoundError, Exception) as e:
            logging.error(f"Falha durante o modo de teste com arquivo local: {e}")
        
        logging.info("--- TESTE DO WEBHOOK CONCLUÍDO. INICIANDO MONITORAMENTO ONLINE. ---")
        time.sleep(3)

    try:
        logging.info(f"Carregando a página inicial pela primeira vez: {DEALS_URL}")
        driver.get(DEALS_URL)
    except WebDriverException as e:
        logging.critical(f"Falha ao carregar a página inicial. Encerrando. Erro: {e}")
        driver.quit()
        return

    processed_deal_names = set()
    is_first_run = True

    try:
        while True:
            try:
                if not is_first_run: 
                    logging.info("Recarregando a página para verificar atualizações...")
                    driver.refresh()
                
                deals = fetch_deals(driver)
            except WebDriverException as e:
                logging.error(f"Erro ao recarregar a página. Tratando como falha: {e}")
                deals = None 

            if deals is None: 
                logging.error("Falha grave detectada. Tentando reiniciar o driver na próxima iteração.")
                driver.quit()
                driver = setup_driver()
                if not driver:
                    logging.critical("Não foi possível reiniciar o driver. Encerrando.")
                    break
                
                try:
                    logging.info(f"Carregando a página inicial com o novo driver: {DEALS_URL}")
                    driver.get(DEALS_URL)
                except WebDriverException as e_inner:
                    logging.critical(f"Falha ao carregar a página inicial após reinício. Encerrando. Erro: {e_inner}")
                    driver.quit()
                    break

                is_first_run = True
                processed_deal_names.clear()
            else: 
                current_deal_names = set(deals.keys())
                if is_first_run:
                    processed_deal_names = current_deal_names
                    is_first_run = False 
                    logging.info(f"Verificação inicial completa. {len(processed_deal_names)} ofertas estão sendo rastreadas.")
                else:
                    new_deals = current_deal_names - processed_deal_names
                    if new_deals:
                        logging.info(f"Encontrada(s) {len(new_deals)} nova(s) oferta(s)!")
                        for deal_name in new_deals:
                            deal_details = deals[deal_name]
                            send_notification(deal_name, deal_details, webhook_url)
                            save_debug_file(driver.page_source, deal_name)
                    else:
                        logging.info("Nenhuma oferta nova encontrada.")
                
                processed_deal_names = current_deal_names

            logging.info(f"Aguardando {POLLING_INTERVAL_SECONDS} segundos para a próxima verificação...")
            time.sleep(POLLING_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        logging.info("Script interrompido pelo usuário.")
    finally:
        if driver:
            logging.info("Encerrando o driver do Chrome.")
            driver.quit()

if __name__ == "__main__":
    main()
