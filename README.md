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

<h1>Deal Watcher by V4 Percus</h1>

<h2>O que eu preciso saber antes de utilizar o Deal Watcher?</h2>
  Este programa foi feito para rodar em qualquer distribuição Linux, recomenda-se virtualizar, e enquanto o programa estiver funcionando não pode haver outra instância do Google Chrome rodando no sistema operacional.

<h2>O que eu preciso instalar/configurar no computador antes de estar pronto para executar o programa?</h2>
Para que o o programa funcione os itens abaixo devem ser configurados, as explicações necessárias estão mais adiate neste documento.
- Baixar este repositório.
- Python instalado [python.org](url);
- Pip instalado [https://pypi.org/project/pip/](url);
- Selenium pip instalado [https://pypi.org/project/selenium/](url);
- Webdriver-manager pip instalado [https://pypi.org/project/webdriver-manager/](url);
- beautifulsoup4 pip [https://pypi.org/project/beautifulsoup4/](url);
- Navegador Google Chrome em sua versão atualizada normal [google.com/chrome](url);
- Chrome for testing [https://googlechromelabs.github.io/chrome-for-testing/](url);
- Chrome driver [https://googlechromelabs.github.io/chrome-for-testing/](url);
- Endereço de webhook onde os deal serão enviados.

<h2>Como instalar arquivos do repositório?</h2>
1. Baixe o arquivo dealWatcher.py no repositório https://github.com/percus-lab/deal-watcher
2. Coloque o arquivo em um pasta separada como, por exemplo: /home/seu-nome-de-usuario/Documentos/reps/deal-watcher/dealWatcher.py

<h2>Como instalar Python, e os pacotes Pip?</h2>
1. Instale o Python no seu sistema linux, em casos de sistemas baseados em Debian, pode se usar o comando a baixo:
  sudo apt install python
2. Instale o Pip, se necessário:
  sudo apt install python-pip
4. Instale os pacotes pip executando os comandos a seguir:
  pip install selenium
  pip install webdriver-manager
  pip install bs4

<h2>Como instalar o Chrome for testing?</h2>
1. Para fazer da download da ultima versão do Chrome for Testing, acesse a página [https://googlechromelabs.github.io/chrome-for-testing/](url) copie a URL do Binary: chrome, e Plataform: linux64, no seu navegador ;
<img width="1772" height="510" alt="image" src="https://github.com/user-attachments/assets/9c872a40-4eae-426b-8549-400fe2fa9d9e" />
Copie a URL em destaque na imagem para uma nova aba no navegador ;
2. Após baixar o arquivo chrome-linux64.zip extraia-o para uma pasta com seu nome, em um diretório permanente, como por exemplo; /home/seu-nome-de-usuario/Documentos/chrome-linux64 (Lembre-se de substituir seu-nome-de-usuario pelo nome do seu usuário no sistema operacional);
3. Copie o caminho do binário chrome que está na pasta, por exemplo: /home/seu-nome-de-usuario/Documentos/chrome-linux64/chrome ;
4. Abra para edição o arquivo dealWatcher.py e cole o caminho copiado na Constante de Configuração CHROME_BINARY_LOCATION, por exemplo: CHROME_BINARY_LOCATION="/home/seu-nome-de-usuario/Documentos/reps/deal-watcher/depens/chrome-linux64/chrome" .

<h2>Como instalar o Chrome Driver?</h2>
1. Para fazer da download da ultima versão do Chrome Driver, acesse a página [https://googlechromelabs.github.io/chrome-for-testing/](url) copie a URL do Binary: chromedriver, e Plataform: linux64, no seu navegador ;
<img width="1745" height="471" alt="image" src="https://github.com/user-attachments/assets/f735b117-10c9-4390-93ec-89d0922b5252" />
Copie a URL em destaque na imagem para uma nova aba no navegador ;
2. Após baixar o arquivo chromedriver-linux64.zip extraia-o na pasta de downloads.
3. Utilize o comando abaixo para mover o arquivo chromedriver de dentro da pasta baixada para o path do seu Linux:
  sudo mv /home/seu-nome-de-usuario/Downloads/chromedriver-linux64/chromedriver /usr/local/bin
4. Utilize o comando abaixo para tornar executavel seu chromedriver recém copiado
  sudo chmod -x /usr/local/bin/chromedriver

<h2>Como extrair as informações de login da conta do Google que vai utilizar o Deal Broker?</h2>
1. Instale a versão regular do  Google Chrome [google.com/chrome](url)
2. Logue no navegador com a conta Google que será utilizada para o Deal Broker;
3. Feche o navegador;
4. Copie o caminho a seguir /home/seu-nome-de-usuario/.config/google-chrome/
5. Abra com um editor de texto o arquivo dealWatcher.py, e cole o caminho na constante de configuração CHROME_USER_DATA_DIR, por exemplo:
  CHROME_USER_DATA_DIR="/home/seu-nome-de-usuario/.config/google-chrome" 

<h2>Onde eu coloco a URL do meu webhook?</h2>
Cole a URL do seu webhook na constante de configuração WEBHOOK_URL, por exemplo:
WEBHOOK_URL= "https://zapier.com.br/webhook/b83cad5f-2a0f-4fa3-a9bf-efc3c5d9ec4"



