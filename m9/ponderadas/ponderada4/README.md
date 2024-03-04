# Ponderada 4
## Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 9 | 2

## Descrição
O objetivo da segunda atividade ponderada 2 de programação consiste em aplicar o método TDD em cima da ponderada 1, um simulador de dispositivos IoT utilizando o protocolo MQTT através do uso da biblioteca Eclipse Paho.

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
- Go 1.22.0
- COnta na HiveMQ

## Instalação
Para instalação, basta abrir um terminal e digitar os seguintes comandos:

```bash
sudo go mod init paho-go
```
após isso

```bash
sudo go mod tidy
```

## Execução
Para executar o projeto, basta seguir os passos abaixo em 4 terminais diferentes:

Execução do mosquitto: 

```bash
mosquitto -c mosquitto.conf
```

```bash
go run publisher.go
```

```bash
go run sub/subscriber.go
```

Por último, para executar o objetivo dessa atividade, no último terminal, execute:

```bash
go test -v -cover
```



Abaixo está contido um vídeo exemplificando o funcionamento do projeto: 

https://drive.google.com/file/d/10JqoGPa8WE64GJ_50Frk0_D4rs3wcmF8/view?usp=sharing
