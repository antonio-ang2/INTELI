# Ponderada Semana 5

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 7 | 2

## Estrutura de Pastas
```
📦semana 5
 ┣ 📜Dockerfile
 ┣ 📜minha_api.pkl
 ┣ 📜minha_api.py
 ┣ 📜modelo_2.pkl
 ┣ 📜requirements.txt
 ┣ 📜READ.MD
```
## Explicação da Atividade
A atividade proposta demanda conceitos de docker e machinelearning. O objetivo é enviar uma imagem docker de um  modelo machine learning gerado pelo Pycaret do aluno para o dockerhub. O Pycaret é um automl que testa modelos com base em um dataset e retorna o melhor modelo para aquele dataset, bem como o melhor tratamento com aquelas determinadas features.

**Link para o DockerHub**: https://hub.docker.com/repository/docker/antonioangelo2/entrega5/general

## Como Executar:
### Localmente
Para fazer o pull da imagem contida no dockerhub basta usar o seguinte comando no terminal: 
```docker push antonioangelo2/entrega5:tagname```

Após isso, rode o comando ```docker images``` para garantir que a imagem está contida no docker.

Rode o comando ```docker run -d --name <nome-do-seu-container> -p 8000:8000 antonioangelo2/entrega5:v1.0``` para criar um container e rodá-lo, a fim de executar a aplicação.

Após isso, projeto pode ser acessado em **(http://localhost:8000)**

Pronto. tudo certo para requisitar uma predição. Agora basta usar a URL do modelo com a API específica (http://localhost:8000/predict).

O dataset escolhido trata-se de um dataset de score de gasto com base nas seguintes características: gênero, idade, Income(quanto de dinheiro esse consumidor ganha anualmente em milhares). Fora esses, o Id costumer também estava contido no dataset, porém, ao gerar o Pycaret, optei por ignorar essa feature, pois se trata de uma feature irrelevante ao modelo.
<br>

Por fim, para rodar o modelo, basta acessar um softare de teste de API, thunderclient, por exemplo, e passar um Json semelhante a essa na URL específica do modelo
{
    "Gender": "Male",
    "Age": 30,
    "Income": 15
}

O resultado esperado é um retorno de predição do score de gasto.


