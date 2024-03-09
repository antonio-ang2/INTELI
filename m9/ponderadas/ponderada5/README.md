# Ponderada 5
## Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 9 | 2

## Descrição
O objetivo da atividade ponderada 5 de programação consiste em integrar todo o projeto até agora realizado, pub/sub com broker, a um banco de dados local que vai ser consumido pelo metabase a fim de criar uma visualização. O banco de dados escolhido para a atividade foi o sqlite, pub/sub com python, mosquitto como broker e docker compose para subir a aplicação toda.

## Estrutura de Arquivos
ponderada2
 ┣ 📜publisher.go
 ┣ 📜subscriber.go
 ┣ 📜README.md
 ┣ 📜go.mod
 ┣ 📜go.sum
 ┣ 📜simulation_test.go
 ┗ 📜mosquitto.config

## Dependências
- python 
- docker
- mosquitto


## Execução
Para executar o projeto, basta seguir os passos abaixo em 4 terminais diferentes:

Execução do mosquitto: 

Roda o broker para permitir conexão do pub/sub
```bash
mosquitto -c mosquitto.conf
```

Cria o banco de dados para armazenar as informações
```bash
python sqlite.py
```

Executa o publisher para criação aleatória de dados, simulando um dispositivo IoT
```bash
python publisher.py
```

Executa o Subscriber, que recebe as informações postadas e as armazena no banco

```bash
python subscriber.py
```

Por fim, para executar o metabase e poder ver suas visualizações, execute

```bash
docker compose up
```


Nicola, meu bem, crie uma conta e crie uma visualização. Usei uma conta real e estou morto de preguiça de criar mais uma. ;)


Abaixo está contido um vídeo exemplificando o funcionamento do projeto: 

https://drive.google.com/file/d/1j2kei_SgitBpLVe9lsQTF1AHoUy_QpYz/view?usp=drive_link


vídeo longo do carai, fique a vontade para pular.