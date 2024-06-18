# Ponderada 4

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 10 | 2

## Estrutura de Pastas

## EXPLICAÇÃO DA ATIVIDADE

A atividade proposta demanda conceitos de docker, microsserviços e log. O objetivo criar uma API em microsserviços, com um gateway para lidar com o redirecionamento, um sistema de logs para a aplicação e um compose para subir a aplicação toda. Nesse sentido, optei por fazer três microsserviços e 


# RODANDO A APLICAÇÃO

```bash
# Para rodar a aplicação basta rodar o docker compose para subir a aplicação, da seguinte forma:
docker compose up
# Pronto, agora se você tiver uma ferramenta(por exemplo, Docker desktop) pode ver o container criado e acessá-lo em:
http://localhost:80
# Essa URI nos manda para o gateway, podendo acessar três serviços diferentes bastando adicionar:
http://localhost:8000/service1/docs
# ou 
http://localhost:8000/service2
#ou
http://localhost:8000/login
```

# MICROSSERVIÇOS
Os microsserviços da aplicação são três e consistem em: um login, usando token para controlar acesso, service2 que serve como um pedido de socorro e logs e, por último o service1 que consiste em uma api de removedor de fundo.


[Demonstração](https://drive.google.com/file/d/1otx8CijPy9iEKKFyEFPoFtBA-Mw8uZyD/view?usp=sharing)



