# PONDERADA 2

# INFORMAÇÕES DO ALUNO
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 11 | 2


## DESCRIÇÃO DA ATIVIDADE


A proposta da segunda atividade ponderada visa a implementação de dois lançadores contendo pacotes distintos. O primeiro lançador tem como finalidade inicializar o pacote de navegação, composto por três módulos essenciais: RVIZ para visualização e abertura do NAV2, Gazebo para a exibição visual e o Cartographer. Já o segundo lançador será responsável por ativar o pacote do script desenvolvido pelo aluno, o qual assume a responsabilidade de definir a pose inicial no Gazebo e especificar a trajetória de pose para o robô simulado seguir.

O propósito central dessa atividade é desafiar o aluno a criar um mapa integralmente utilizando as funcionalidades oferecidas pelo NAV2. O enfoque está na avaliação e aplicação dos conhecimentos em ROS2, utilizando pacotes e lançadores de forma coordenada para atingir o objetivo proposto.



## COMO EXECUTAR A ATIVIDADE

Para executar esse projeto, é necessário executar os dois pacotes em terminais diferentes.

- Abra dois terminais e dirija-se à pasta 'meu_workspace'

- No primeiro terminal execute ```ros2 launch my_package test_launch.py```. Com isso, você executará o pacote de mapeamento que inclui: Gazebo, RVIZ e cartographer.

- No segundo terminal execute ```ros2 launch my_package test_launch.py```. Com isso, você executará o pacote de navegação que inclui: script para setar pose inicial e uma pose objetiva.


## VÍDEO DE DEMONSTRAÇÃO    

https://drive.google.com/file/d/1rAhAzNamRjSGZrm9ziTYLxfuygKorCPF/view?usp=sharing
