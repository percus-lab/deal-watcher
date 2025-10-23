> This file is part of Deal Watcher.
>
> Deal Watcher is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, version 3 of the License.
>
> Deal Watcher is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
> GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License
> along with Deal Watcher. If not, see <https://www.gnu.org/licenses/>

# Deal Watcher by V4 Percus

O Deal Watcher é um script de monitoramento automatizado que observa a página de ofertas do Deal Broker. Quando uma nova oferta é detectada, o script envia uma notificação com os detalhes para um webhook pré-configurado.

## O que eu preciso saber antes de utilizar o Deal Watcher?

> [!WARNING]
> Este programa foi feito para rodar em qualquer distribuição Linux. Recomenda-se o uso em um ambiente virtualizado. Enquanto o programa estiver funcionando, **não pode haver outra instância do Google Chrome rodando no sistema operacional**.

## Pré-requisitos

Para que o programa funcione, os itens abaixo devem ser instalados e configurados conforme o guia a seguir:

* O código do Deal Watcher baixado.
* Python instalado.
* Pip instalado.
* Pacotes `selenium`, `webdriver-manager` e `beautifulsoup4`.
* Navegador Google Chrome (versão regular).
* Chrome for testing.
* Chrome Driver.
* Endereço de webhook onde os deals serão enviados.

---

## 1. Como instalar os arquivos do repositório?

1.  Baixe o arquivo `dealWatcher.py` do repositório: [https://github.com/percus-lab/deal-watcher](url).
2.  Coloque o arquivo em uma pasta separada. Por exemplo:
    ```bash
    /home/seu-nome-de-usuario/Documentos/reps/deal-watcher/dealWatcher.py
    ```

## 2. Como instalar o Python e os pacotes Pip?

1.  **Instale o Python** no seu sistema Linux. Para sistemas baseados em Debian:
    ```sh
    sudo apt install python
    ```
2.  **Instale o Pip**, se necessário:
    ```sh
    sudo apt install python-pip
    ```
3.  **Instale os pacotes Pip** necessários com os seguintes comandos:
    ```sh
    pip install selenium webdriver-manager bs4
    ```

## 3. Como instalar e configurar o Chrome for Testing?

1.  Acesse a página de downloads do [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
2.  Copie a URL do **Binary** referente ao `chrome` na plataforma `linux64` e use-a para baixar o arquivo `chrome-linux64.zip`.<img width="1691" height="418" alt="image" src="https://github.com/user-attachments/assets/9c0ad5ec-26f5-4690-9b8f-b10b612446b9" />
3.  Extraia o arquivo para uma pasta permanente. Por exemplo:
    ```bash
    /home/seu-nome-de-usuario/Documentos/chrome-linux64
    ```
4.  Copie o caminho completo do binário `chrome` que está dentro da pasta extraída. Por exemplo:
    ```bash
    /home/seu-nome-de-usuario/Documentos/chrome-linux64/chrome
    ```
5.  **Abra o arquivo `dealWatcher.py`** e cole o caminho que você acabou de copiar na constante `CHROME_BINARY_LOCATION`. Por exemplo:
    ```python
    CHROME_BINARY_LOCATION="/home/seu-nome-de-usuario/Documentos/reps/deal-watcher/depens/chrome-linux64/chrome"
    ```

## 4. Como instalar o Chrome Driver?

1.  Na mesma página do [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/), copie a URL do **Binary** referente ao `chromedriver` na plataforma `linux64` para baixar o arquivo.<img width="1679" height="519" alt="image" src="https://github.com/user-attachments/assets/264ef38c-4738-4185-aa2e-75db3e1d296d" />
2.  Após baixar, extraia o arquivo `chromedriver-linux64.zip` na sua pasta de downloads.
3.  Mova o arquivo `chromedriver` para um diretório no PATH do seu sistema, para que ele possa ser encontrado pelo script. Um local comum é `/usr/local/bin`:
    ```sh
    sudo mv /home/seu-nome-de-usuario/Downloads/chromedriver-linux64/chromedriver /usr/local/bin
    ```
4.  Dê permissão de execução ao arquivo:
    ```sh
    sudo chmod +x /usr/local/bin/chromedriver
    ```

## 5. Como configurar os dados de login?

Para que o script acesse o Deal Broker, ele precisa dos dados do seu perfil do Chrome.

1.  Instale e faça login no Google Chrome (versão regular) com a conta Google que será utilizada no Deal Broker.
2.  Para confirmar, também logue na plataforma do Deal Broker [https://deal.brokers.mktlab.app/](url).
3.  Feche o navegador completamente.
4.  Ainda no arquivo `dealWatcher.py`, localize a constante `CHROME_USER_DATA_DIR` e cole o caminho para o diretório de configuração do Chrome. Por exemplo:
    ```python
    CHROME_USER_DATA_DIR="/home/seu-nome-de-usuario/.config/google-chrome"
    ```

## 6. Como configurar o webhook?

1.  No arquivo `dealWatcher.py`, localize a constante `WEBHOOK_URL` e cole a URL do seu webhook. Por exemplo:
    ```python
    WEBHOOK_URL="[https://zapier.com.br/webhook/b83cad5f-2a0f-4fa3-a9bf-efc3c5d9ec4](https://zapier.com.br/webhook/b83cad5f-2a0f-4fa3-a9bf-efc3c5d9ec4)"
    ```

## 7. Como executar o programa?

Após concluir toda a configuração:

1.  Abra um terminal.
2.  Navegue até o diretório onde você salvou o arquivo `dealWatcher.py`.
3.  Execute o script com o comando:
    ```sh
    python3 dealWatcher.py
    ```
