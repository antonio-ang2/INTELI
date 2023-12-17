# Ponderada Semana 1 

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 7 | 2

## Estrutura de Pastas
```
📦semana 1
 ┣ 📂amb
 ┃ ┣ 📂Include
 ┃ ┣ 📂Lib
 ┃ ┣ 📂Scripts
 ┃ ┣ 📂static
 ┃ ┣ 📜Dockerfile
 ┃ ┣ 📜main.py
 ┃ ┣ 📜pyvenv.cfg
 ┃ ┣ 📜requirements.txt
 ┣ 📜READ.MD
```
## Explicação da Atividade
A atividade proposta demanda conceitos de docker e desenvolvimento web. O objetivo é enviar uma imagem docker do currículo do aluno para o dockerhub.
**Link para o DockerHub**: 

## Como Executar:
### Localmente
Fazendo a build da imagem contida arquivo Dockerfile, o projeto pode ser executado com o seguinte comando em um terminal de sua preferência:
```
docker build -t <nome-da-sua-imagem> .
docker run -d --name <nome-do-seu-container> -p 80:80 <nome-da-sua-imagem>
```
Após isso, projeto pode ser acessado em **[localhost](http://localhost:80)**.

### Via Docker Hub
Basta acessar o link da imagem criada, **[antonioangelo2/entrega1](https://hub.docker.com/repository/docker/antonioangelo2/entrega1/general)** e com isso, rodar os seguintes comandos no terminal de sua preferência:
```
docker push antonioangelo2/entrega1:tagname
docker run -d --name mycontainer -p 80:80 antonioangelo2/entrega1:v1.0
```
Após isso, projeto pode ser acessado em **[localhost](http://localhost:80)**.


