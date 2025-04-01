# Projeto de Análise Imobiliária - Scraping de Imóveis
Este projeto utiliza técnicas de web scraping para coletar dados sobre imóveis de um site imobiliário e salvar as informações em um arquivo CSV. O objetivo é realizar uma análise sobre o mercado imobiliário com base nos dados coletados

Tecnologias Utilizadas
Python: Linguagem de programação utilizada para o desenvolvimento do script.
Selenium: Ferramenta usada para automação de navegadores e para buscar a página web com os dados.
BeautifulSoup: Biblioteca para parseamento e extração de dados HTML.
CSV: Formato utilizado para exportar os dados coletados.

Como Funciona
Automação do Navegador: O script utiliza o Selenium para abrir o site https://www.niponimoveis.com.br de forma automatizada.
Coleta de Dados: Com o BeautifulSoup, o script faz o parseamento do HTML da página e extrai informações como título, preço e localização dos imóveis.
Exportação de Dados: Após coletar as informações, os dados são salvos em um arquivo CSV chamado imoveis.csv.

Pré-requisitos
Antes de executar o script, você precisa ter os seguintes pacotes instalados: bash, pip install selenium,pip install beautifulsoup4

Estrutura do Código
O código do projeto está organizado da seguinte forma:
MercadoImobiliario/
│
├── Scripts/
│   └── Scraping.py  # Código responsável pelo scraping de dados dos imóveis
└── imoveis.csv      # Arquivo CSV com os dados coletados

Scraping.py
O script Scraping.py realiza as seguintes etapas: Configuração do Selenium: Configura o driver do Chrome para rodar em modo headless (sem abrir uma janela do navegador).
Acessa o Site: Carrega a página com os dados dos imóveis.
Extração de Dados: Coleta o título, preço e localização de cada imóvel na página.
Exportação para CSV: Salva os dados coletados no arquivo imoveis.csv.

Como Executar
Clone o repositório para sua máquina local: git clone <URL do repositório>
Acesse o diretório onde o script está localizado:cd MercadoImobiliario/Scripts
Execute o script Python:python Scraping.py

Contribuições
Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma pull request. Caso tenha alguma dúvida ou sugestão, abra uma issue ou entre em contato comigo 11966478060.
