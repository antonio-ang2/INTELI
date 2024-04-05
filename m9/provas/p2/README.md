# Prova 2
## Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 9 | 2

## Descrição
O objetivo da parte prática da segunda prova é criar uma simulação de clientes(consumer/producer), conectá-lo ao kafka e testar esta conexão.
## Estrutura de Arquivos
ponderada1
 ┣ 📜static
 ┣ 📜docker-compose.yml
 ┣ 📜kafka-python.py
 ┗ 📜README.md

## Dependências
- Imagens do Zookeeper e do Kafka

## Instalação
Para instalação, basta abrir um terminal no diretório p2 e digitar o seguinte comando:

```bash
docker-compose up -d
```

Com isso, as imagens do zookeeper e kafka irão ser instaladas na máquina e o cluster irá iniciar.

## Execução
Para executar o projeto, basta seguir os passos abaixo:

Execução do arquivo consumer/producer: 
```bash
python3 kafka-python.py
```

Demonstração:

A fim de demonstrar o processo de criação do armotecedor de cidades inteligentes, tirei alguns prints como melhor forma de visualização.

![Conexão com Kafka](../p2/static/kafka1.jpeg)

