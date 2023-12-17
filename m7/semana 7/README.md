# Ponderada Semana 5

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 7 | 2

## Estrutura de Pastas
```
📦semana 7
 ┣ 📂amb
 ┃ ┣ 📂Include
 ┃ ┣ 📂Lib
 ┃ ┣ 📂Scripts
 ┃ ┣ 📂share
 ┃ ┣ 📜pyvenv.cfg
 ┣ 📂pages
 ┣ 📂content
 ┣ 📜pyvenv.cfg
 ┣ 📜Dockerfile
 ┣ 📜logs.log
 ┣ 📜main.py
 ┣ 📜minha_api.pkl
 ┣ 📜minha_api.py
 ┣ 📜modelo_2.pkl
 ┣ 📜READ.MD
 ┣ 📜requirements.txt
 ┣ 📜style.css
```
## Descrição da Atividade
A atividade proposta envolve o uso de vários serviços e tecnologias, incluindo AWS (Amazon Web Services), PyCaret, Streamlit e FastAPI, para criar uma aplicação que aceita um arquivo CSV como entrada, envia-o para um modelo de machine learning e retorna as previsões em formato JSON. O objetivo é prever o "Spending Score" com base em dados de um conjunto de dados chamado "Customer Segmentation". O conjunto de dados inclui as seguintes colunas:

CustomerID
Gender
Age
Annual Income (k$) (renomeado para "Income" por questões de praticidade)
Spending Score (1-100) (renomeado para "Score" por questões de praticidade)
Tecnologias Utilizadas
Streamlit
Descrição: Streamlit é uma ferramenta de código aberto que permite a criação de aplicativos web de forma simples, sem a necessidade de conhecimentos avançados em desenvolvimento frontend. Neste projeto, o Streamlit é usado para criar uma interface de usuário para carregar arquivos CSV, exibir gráficos e enviar os dados para o modelo de machine learning.

Estrutura: A estrutura do projeto inclui um diretório chamado "pages" onde o Streamlit é utilizado para criar diferentes páginas, incluindo uma página para carregar o arquivo CSV e outra página para visualizar as previsões.

Visualizações: O Streamlit exibe três tipos de gráficos diferentes: um gráfico de comparação entre idade e "Select data" (que pode ser "Income" ou "Score"), além de histogramas que relacionam idade com frequência e frequência com "Select data".

## AWS - EC2
Descrição: O Amazon Elastic Compute Cloud (Amazon EC2) é um serviço de computação em nuvem que permite a criação e gerenciamento de máquinas virtuais escaláveis em um ambiente de nuvem. No projeto, um aluno criou uma instância EC2 na AWS para hospedar a aplicação.

Instância EC2: O aluno criou uma instância EC2 para hospedar a aplicação. Uma imagem da instância em execução é exibida na imagem chamada "instance.png".

## Modelo e Backend
PyCaret: PyCaret é uma biblioteca em Python que simplifica o desenvolvimento e implantação de modelos de machine learning. Foi utilizado para treinar um modelo de machine learning com base no conjunto de dados "Customer Segmentation". O modelo é exportado em um arquivo PKL.

FastAPI: FastAPI é um framework web em Python usado para criar APIs de maneira rápida e fácil. Foi utilizado como o backend da aplicação para receber os arquivos CSV, carregar o modelo treinado e retornar as previsões em formato JSON.

## Como Executar o Projeto Localmente
### Localmente
Para executar o projeto localmente, siga os seguintes passos:

Baixe o arquivo do projeto do GitHub disponibilizado pelo aluno.

Navegue até a pasta chamada "amb" no projeto e entre na pasta "Scripts". Em seguida, ative o ambiente virtual executando o comando ```activate```.

Volte para o diretório raiz do projeto.

Instale as dependências do projeto executando o comando ```pip install -r requirements.txt".```

Navegue até a pasta "Semana 7" no projeto e execute o seguinte comando para iniciar o servidor FastAPI:

```uvicorn main:app --host 0.0.0.0 --port 8000```

Abra um segundo prompt de comando, navegue até a pasta "Semana 7" novamente e execute o seguinte comando para iniciar a aplicação Streamlit:
```streamlit run main.py```

A aplicação estará disponível localmente em **( http://localhost:8501)**

Dessa forma, você poderá interagir com a aplicação, carregar arquivos CSV, visualizar gráficos e obter previsões com base no modelo de machine learning treinado. Certifique-se de que todas as etapas anteriores tenham sido executadas corretamente para garantir o funcionamento adequado do projeto.




