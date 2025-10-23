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

Deal Watcher by V4 Percus

O que eu preciso saber antes de utilizar o Deal Watcher?
  Este programa foi feito para rodar em qualquer distribuição Linux, recomenda-se virtualizar, e enquanto o programa estiver rodando não pode haver outra instância do Google Chrome no sistema operacional.

O que eu preciso instalar/configurar no computador antes de estar pronto para executar o programa?
Para que o o programa funcione os itens abaixo devem ser configurados, as explicações necessárias estão mais adiate neste documento.
- Python instalado [python.org](url);
- Pip instalado [https://pypi.org/project/pip/](url);
- Selenium pip instalado [https://pypi.org/project/selenium/](url);
- Webdriver-manager pip instalado [https://pypi.org/project/webdriver-manager/](url);
- beautifulsoup4 pip [https://pypi.org/project/beautifulsoup4/](url);
- Navegador Google Chrome em sua versão atualizada normal [google.com/chrome](url);
- Chrome for testing [https://googlechromelabs.github.io/chrome-for-testing/](url);
- Chrome driver [https://googlechromelabs.github.io/chrome-for-testing/](url);

-Como instalar Python, e os pacotes Pip?
1. Instale o Python no seu sistema linux, em casos de sistemas baseados em Debian, pode se usar o comando a baixo:
    sudo apt install python
2. Instale o Pip, se necessário:
    sudo apt install python-pip
3. Instale os pacotes pip executando os comandos a seguir:
  pip install selenium
  pip install webdriver-manager
  pip install bs4

-Como instalar o Chrome for testing?
