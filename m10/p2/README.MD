# P2 - PARTE PRÁTICA - Flask para Fastapi com docker compose e logs

# OBJETIVO DA PARTE PRÁTICA
O objetivo da parte prática da segunda prova é incremnetar uma API com maturidade 2 já existente. A API foi feita em Flask e nossa tarefa é incrementá-la, usando a lib FastAPI para modificá-la, colocar em conteiner, adicionar logs e um gateway para lidar com outros microsserviços. 

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

Essa aplicação consiste em uma API assincrona de criação de posts em um blog, contento as seguintes informações referentes ao post: title e content. É uma aplicação dockerizada, com gateway e logs.

[Demonstração](https://drive.google.com/file/d/1TU3FdR6Ipkz_gWLHqZDiqmba-uZynhVg/view?usp=sharing)

