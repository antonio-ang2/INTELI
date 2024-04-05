# Prova 2
## Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 9 | 2

## Descrição
O objetivo da parte prática da segunda prova é criar uma simulação de clientes(pub/sub), com teste de e testar sua conexão com o broker, mosquitto.

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

