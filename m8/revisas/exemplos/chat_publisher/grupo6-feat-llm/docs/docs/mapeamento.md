---
sidebar_position: 6
slug: '/mapeamento'
---

# Sistema de localização e mapeamento simultâneo
O sistema de mapeamento e navegação enfoca o procedimento essencial que capacita um robô a movimentar-se de maneira autônoma em um ambiente desconhecido. Inicialmente, abordaremos o método pelo qual o robô constrói um mapa do ambiente ao seu redor, identificando obstáculos e possíveis trajetos. Em seguida, exploraremos a relevância de uma interface de comunicação eficiente que capacita os usuários a especificar destinos nos quais desejam que o robô se desloque. Essa interface organiza esses destinos em uma sequência lógica e os transmite ao robô na ordem adequada. A integração fluida entre o mapeamento e a comunicação é crucial para a autonomia do robô. Abaixo, detalharemos cada etapa desse processo, elucidando como cada componente contribui para a operação autônoma eficiente do robô.

## Desenvolvimento
### Tecnologias
As principais tecnologias utilizadas para a construção de um veículo autonômo foi uma combinação entre o ROS 2 (Robot Operating System 2), NAV2 (Navigation Stack 2) e TurtleBot3, que podem ser aplicadas em uma implementação de navegação autônoma em ambientes industriais. 

O ROS 2 desempenha um papel essencial como sistema operacional para robôs, proporcionando uma base sólida para o desenvolvimento. Integrado ao ecossistema ROS 2, o NAV2 complementa essa estrutura ao fornecer recursos avançados de navegação, que abrangem algoritmos de mapeamento, localização e planejamento de trajetória. Essa sinergia entre o ROS 2 e o NAV2 estabelece uma plataforma abrangente e robusta, impulsionando eficazmente o desenvolvimento de sistemas autônomos com capacidades avançadas de navegação.

No cenário abordado, o TurtleBot3 é caracterizado por sua modularidade e flexibilidade, integrando-se ao ROS 2 e NAV2 e consolidando-se como uma plataforma pronta para aplicação prática. Essa combinação de tecnologias viabiliza o desenvolvimento de soluções autônomas e eficazes para robôs destinados à entrega de ferramentas em ambientes industriais. O TurtleBot3, ao aproveitar a navegação autônoma proporcionada pelo NAV2 e a infraestrutura do ROS 2, pode ser programado para navegar de maneira inteligente, otimizando rotas, contornando obstáculos e realizando entregas autônomas.

No contexto de nosso projeto, essa sequência de tecnologias estabelece uma base robusta para a automação e eficiência nas operações logísticas internas. A interação entre ROS 2, NAV2 e TurtleBot3 tem como objetivo impulsionar a navegação autônoma de robôs destinados à entrega de ferramentas, representando um avanço significativo na aplicação de tecnologias de última geração para aprimorar as operações industriais. Esta documentação destaca a complementaridade entre essas tecnologias, evidenciando como elas se entrelaçam para formar uma solução integrada e eficaz em consonância com os objetivos de nosso projeto.

### Módulos
Este projeto é dividido em dois workspaces localizados na pasta src. O primeiro workspace é dedicado ao mapeamento, enquanto o segundo lida com a navegação.

#### Mapeamento 

#### Navegação 
No ambiente de navegação, um pacote específico foi desenvolvido dentro do workspace. Esse pacote inclui um script em bash projetado para iniciar o Rviz, um visualizador 3D para ROS, utilizando um arquivo de mapa como argumento. Além disso, foram implementados quatro nós distintos:

1. Um nó destinado a abrir um terminal de chatbot.
2. Outro nó projetado para abrir um terminal responsável pela entrada de coordenadas.
3. Um nó adicional encarregado de inicializar a pose do robô.
4. Um nó para gerenciar a fila de pontos relacionados à navegação.

É relevante observar que o nó responsável pela inicialização da pose do robô é concebido de maneira efêmera, encerrando-se automaticamente após a publicação da pose. Em contraste, os outros nós permanecem ativos durante toda a interação do usuário, desempenhando papéis específicos no contexto da navegação. Essa arquitetura proporciona uma integração eficiente e funcional para o controle e visualização do robô em seu ambiente.

**Execução**

Para executar a navegação, utilize os seguintes comandos na pasta raiz do workspace:
```
colcon build
source install/setup.bash
bash run.sh <nome-do-mapa>.yaml
```

## Testes
### Sprint 2
O vídeo abaixo representa o resultado do processo de desenvolvimento da primeira versão do nosso sistema de mapeamento e navegação. 



Através deste primeiro registro, será possível acompanhar a evolução e os desafios enfrentados na criação do método fundamental que permite ao robô movimentar-se autonomamente em ambientes desconhecidos. Desde a construção do mapa do ambiente até a integração com uma interface de comunicação eficiente para direcionar os destinos desejados.





