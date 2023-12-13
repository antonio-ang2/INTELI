# PONDERADA 3

# INFORMAÇÕES DO ALUNO
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 8 | 2


## DESCRIÇÃO DA ATIVIDADE


A proposta da terciera atividade ponderada visa a implementação de um chatbot com interface CLI. Esse chat usaria expressões regulares, ou regex, para percorrer as mensagens forncecidas pelo usuário e encontrar um intenção específica que o usuário possa ter tido. Dessa forma, essa intenção seria vinculada a um dicionário de pontos, com coordenadas cartesianas para o robô. Um exemplo de uso seria, mandar o robô andar até o ponto x, que está contido no dicionário de pontos e representa o ponto ("x": [2.0, 2.0, 0.0]).

O propósito central dessa atividade é desafiar o aluno a criar um chat de interação por meio do CLI. Optei por realizar a resposta do chat por meio de uma publicação do chat para o tópico nav2 que faz o robô movimentar-se.



## COMO EXECUTAR O PROJETO

Para executar esse projeto, é necessário executar os dois pacotes em terminais diferentes.

- Abra dois terminais e dirija-se à pasta 'workspace'

- No primeiro terminal execute ```ros2 run ola_mundo chat.py```. Com isso, você executará o pacote do chat, com ele, você definirá a pose inicial, transformação para quaternions e, por fim, execução de um chatbot por meio do CLI.

- No segundo terminal execute ```ros2 launch turtlebot3_gazebo turtlebot_world.launch.py```. Com isso, você executará o pacote do Gazebo, a fim de receber a resposta do chatbot, ou seja, a movimentação do robô.


## VÍDEO DE DEMONSTRAÇÃO    

https://drive.google.com/file/d/1g8oC2FRW5kzh0N7EcLQsbLK8wDI4DS54/view?usp=drive_link









