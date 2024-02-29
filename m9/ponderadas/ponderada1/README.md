# Ponderada 1 
## Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 9 | 2

## Descrição
O objetivo da atividade ponderada 1 consiste em criar um simulador de dispositivos IoT utilizando o protocolo MQTT através do uso da biblioteca Eclipse Paho.

## Estrutura de Arquivos
ponderada1
 ┣ 📜publisher.py
 ┣ 📜subscriber.py
 ┣ 📜README.md
 ┗ 📜mosquitto.config

## Dependências
- Python 3.9 ou superior
- Mosquitto

## Instalação
Para instalação, basta abrir um terminal e digitar o seguinte comando:

```bash
sudo apt-get install mosquitto mosquitto-clients
```

## Execução
Para executar o projeto, basta seguir os passos abaixo:

Execução do mosquitto: 
```bash
mosquitto -c mosquitto.conf
```

Para execução, execute em dois terminais diferentes:
```bash
python publisher.py
python subscriber.py
```


Abaixo está contido um vídeo exemplificando o funcionamento do projeto: 

https://drive.google.com/file/d/1deQwAWFhrgjnqhTfDU-FRBEalYP3nVm2/view?usp=drive_link
