# Deal Watcher por V4 Percus

O Deal Watcher é um script de monitoramento automatizado projetado para observar a página de ofertas do Deal Broker. Quando uma nova oferta é detectada, o script envia uma notificação instantânea com os detalhes da oferta para um webhook pré-configurado.

## Sobre o Software (Licença)

[cite_start]Este projeto é um software livre: você pode redistribuí-lo e/ou modificá-lo sob os termos da Licença Pública Geral GNU, conforme publicada pela Free Software Foundation, na versão 3 da licença[cite: 1].

[cite_start]O Deal Watcher é distribuído na esperança de que seja útil, mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM FIM ESPECÍFICO[cite: 2, 3]. [cite_start]Para mais detalhes, consulte a [Licença Pública Geral GNU](https://www.gnu.org/licenses/)[cite: 4, 5].

## ⚠️ Aviso Importante

> [cite_start]Este programa foi projetado para rodar em qualquer distribuição Linux[cite: 5]. Recomenda-se o uso em um ambiente virtualizado. [cite_start]Para que o script funcione corretamente, **nenhuma outra instância do Google Chrome pode estar rodando** no sistema operacional durante a execução do programa[cite: 5].

## ✅ Pré-requisitos

Antes de iniciar a configuração, garanta que você tenha os seguintes itens instalados no seu sistema:

* [cite_start][Python](https://www.python.org/) [cite: 7]
* [cite_start][Pip (gerenciador de pacotes Python)](https://pypi.org/project/pip/) [cite: 7]
* [cite_start]O navegador [Google Chrome (versão regular)](https://www.google.com/chrome/) instalado e atualizado[cite: 8].
* [cite_start]Um endereço de webhook para receber as notificações das ofertas[cite: 9].

## ⚙️ Guia de Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e deixar o Deal Watcher pronto para ser executado.

### Passo 1: Baixar os Arquivos do Repositório

1.  [cite_start]Baixe o arquivo `dealWatcher.py` do repositório [https://github.com/percus-lab/deal-watcher](https://github.com/percus-lab/deal-watcher)[cite: 10].
2.  Crie uma pasta dedicada para o projeto e coloque o arquivo dentro dela. [cite_start]Por exemplo[cite: 10]:
    ```bash
    /home/seu-nome-de-usuario/Documentos/reps/deal-watcher/dealWatcher.py
    ```

### Passo 2: Instalar Python e Pacotes Necessários

1.  [cite_start]**Instale o Python.** Em sistemas baseados em Debian (como o Ubuntu), você pode usar o comando[cite: 10]:
    ```sh
    sudo apt install python
    ```
2.  [cite_start]**Instale o Pip**, caso não esteja presente[cite: 10]:
    ```sh
    sudo apt install python-pip
    ```
3.  [cite_start]**Instale as bibliotecas Python** necessárias para o projeto com os seguintes comandos[cite: 10]:
    ```sh
    pip install selenium
    pip install webdriver-manager
    pip install bs4
    ```

### Passo 3: Instalar o Chrome for Testing

O script utiliza uma versão específica do Chrome, chamada "Chrome for Testing", para automação.

1.  [cite_start]Acesse a página oficial de downloads do [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)[cite: 11].
2.  Na seção de downloads, encontre a versão estável (`Stable`) mais recente.
3.  [cite_start]Localize a linha correspondente ao binário `chrome` para a plataforma `linux64` e copie a URL para baixá-lo[cite: 11].
4.  Extraia o conteúdo do arquivo `.zip` para um diretório permanente. [cite_start]Por exemplo[cite: 13, 14]:
    ```bash
    /home/seu-nome-de-usuario/Documentos/chrome-linux64
    ```
5.  [cite_start]O caminho completo para o executável será algo como[cite: 15]:
    ```bash
    /home/seu-nome-de-usuario/Documentos/chrome-linux64/chrome
    ```
    Guarde este caminho, pois você o usará na etapa de configuração do script.

### Passo 4: Configurar o Script `dealWatcher.py`

Abra o arquivo `dealWatcher.py` em um editor de texto para configurar as constantes principais.

1.  **Configurar o Perfil do Google Chrome (Login)**
    * [cite_start]Faça login no Google Chrome (versão normal) com a conta que tem acesso ao Deal Broker e depois feche o navegador[cite: 21].
    * No arquivo `dealWatcher.py`, localize a constante `CHROME_USER_DATA_DIR` e cole o caminho para o diretório de configuração do Chrome. [cite_start]O padrão é[cite: 21]:
        ```python
        CHROME_USER_DATA_DIR="/home/seu-nome-de-usuario/.config/google-chrome" 
        ```

2.  **Apontar para o Binário do Chrome for Testing**
    * Localize a constante `CHROME_BINARY_LOCATION` e cole o caminho completo para o executável que você extraiu no **Passo 3**. [cite_start]Por exemplo[cite: 16]:
        ```python
        CHROME_BINARY_LOCATION="/home/seu-nome-de-usuario/Documentos/reps/deal-watcher/depens/chrome-linux64/chrome"
        ```

3.  **Definir a URL do Webhook**
    * [cite_start]Localize a constante `WEBHOOK_URL` e insira a URL do seu webhook[cite: 21]. Por exemplo:
        ```python
        WEBHOOK_URL= "[https://zapier.com.br/webhook/b83cad5f-2a0f-4fa3-a9bf-efc3c5d9ec4](https://zapier.com.br/webhook/b83cad5f-2a0f-4fa3-a9bf-efc3c5d9ec4)"
        ```

## ▶️ Executando o Programa

Após concluir toda a instalação e configuração, você pode iniciar o monitoramento.

1.  Abra um terminal.
2.  Navegue até o diretório onde você salvou o arquivo `dealWatcher.py`.
3.  Execute o script com o seguinte comando:
    ```sh
    python3 dealWatcher.py
    ```

O script começará a rodar, e o log de atividades será exibido no terminal e salvo no arquivo `deal_monitor.log`.
