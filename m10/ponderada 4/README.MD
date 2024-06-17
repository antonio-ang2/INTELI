# Ponderada 4

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 10 | 2

## Estrutura de Pastas
```
📦microsservices
 ┣ 📜Dockerfile
 ┣ 📜minha_api.pkl
 ┣ 📜minha_api.py
 ┣ 📜modelo_2.pkl
 ┣ 📜requirements.txt
 ┣ 📜READ.MD
```
## EXPLICAÇÃO DA ATIVIDADE

A atividade proposta demanda conceitos de docker, microsserviços e log. O objetivo criar uma API em microsserviços, com um gateway para lidar com o redirecionamento, um sistema de logs para a aplicação e um compose para subir a aplicação toda. Nesse sentido, optei por fazer três microsserviços e 


# RODANDO A APLICAÇÃO

```bash
# Optei por não criar um env dessa vez, porém, o passo a passo segue parecido com as demais prova.
# criando o banco de dados de blog da nossa aplicação
python cria_banco.py #Esse passo só é necessário se o banco não estiver criado;
# Tudo pronto, após isso basta voltar para raiz e executar
docker compose up
# Pronto, agora se você tiver uma ferramenta(por exemplo, Docker desktop) pode ver o container criado e acessá-lo em:
http://localhost:8000/
# Essa URI nos manda para o gateway, podendo acessar dois serviços diferentes bastando adicionar:
http://localhost:8000/service1
# ou 
http://localhost:8000/service2
```


