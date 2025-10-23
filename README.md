> This file is part of Deal Watcher.
>
> Deal Watcher is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License.
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

## O que eu preciso instalar/configurar no computador?

Para que o programa funcione, os itens abaixo devem ser configurados conforme explicado nas seções seguintes:

* Baixar este repositório.
* Python instalado.
* Pip instalado.
* Pacotes `selenium`, `webdriver-manager` e `beautifulsoup4`.
* Navegador Google Chrome (versão normal).
* Chrome for testing.
* Chrome Driver.
* Endereço de webhook onde os deals serão enviados.

---

## 1. Como instalar arquivos do repositório?

1.  Baixe o arquivo `dealWatcher.py` do repositório: `https://github.com/percus-lab/deal-watcher`.
2.  Coloque o arquivo em uma pasta separada. Por exemplo:
    ```bash
    /home/seu-nome-de-usuario/Documentos/reps/deal-watcher/dealWatcher.py
    ```

## 2. Como instalar Python e os pacotes Pip?

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

## 3. Como instalar o Chrome for Testing?

1.  Acesse a página de downloads do [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
2.  Copie a URL do **Binary** referente ao `chrome` na plataforma `linux64` e use-a para baixar o arquivo `chrome-linux64.zip`.
3.  Extraia o arquivo para uma pasta permanente. Por exemplo:
    ```bash
    /home/seu-nome-de-usuario/Documentos/chrome-linux64
    ```
4.  Copie o caminho completo do binário `chrome` que está dentro da pasta extraída. Você usará este caminho mais tarde. Por exemplo:
    ```bash
    /home/seu-nome-de-usuario/Documentos/chrome-linux64/chrome
    ```

## 4. Como instalar o Chrome Driver?

1.  Na mesma página do [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/), copie a URL do **Binary** referente ao `chromedriver` na plataforma `linux64` para baixar o arquivo.
2.  Após baixar, extraia o arquivo `chromedriver-linux64.zip`.
3.  Mova o arquivo `chromedriver` para um diretório no PATH do seu sistema, para que ele possa ser encontrado pelo script. Um local comum é `/usr/local/bin`:
    ```sh
    sudo mv /caminho/para/chromedriver-linux64/chromedriver /usr/local/bin/
    ```
4.  Dê permissão de execução ao arquivo:
    ```sh
    sudo chmod +x /usr/local/bin/chromedriver
    ```

## 5. Como extrair as informações de login da conta do Google?

Para que o script acesse o Deal Broker já logado, ele precisa dos dados do seu perfil do Chrome.

1.  Instale e faça login no Google Chrome (versão regular) com a conta que será utilizada.
2.  Feche o navegador completamente.
3.  Abra o arquivo `dealWatcher.py` em um editor de texto.
4.  Localize a constante `CHROME_USER_DATA_DIR` e cole o caminho para o diretório de configuração do Chrome. Por exemplo:
    ```python
    CHROME_USER_DATA_DIR="/home/seu-nome-de-usuario/.config/google-chrome"
    ```

## 6. Onde eu configuro os caminhos e o webhook?

Ainda no arquivo `dealWatcher.py`, configure as seguintes constantes:

1.  **Caminho do Chrome for Testing:** Cole o caminho que você copiou no passo 3.4 na constante `CHROME_BINARY_LOCATION`. Por exemplo:
    ```python
    CHROME_BINARY_LOCATION="/home/seu-nome-de-usuario/Documentos/chrome-linux64/chrome"
    ```
2.  **URL do Webhook:** Cole a URL do seu webhook na constante `WEBHOOK_URL`. Por exemplo:
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
