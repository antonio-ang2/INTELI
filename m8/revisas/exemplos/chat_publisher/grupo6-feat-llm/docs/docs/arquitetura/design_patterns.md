---
sidebar_position: 5
slug: '/design_patterns'
---

# Design Patterns

Design Patterns são soluções recorrentes para problemas comuns que surgem durante o desenvolvimento de software. Eles representam as melhores práticas utilizadas por desenvolvedores, facilitando a manutenção e reutilização do sistema.

Até agora, as implementações utilizando Design Patterns têm se concentrado principalmente na aplicação do Strategy Pattern, uma abordagem que oferece flexibilidade ao permitir a definição de uma família de algoritmos, encapsulando cada um deles de maneira independente. A ideia principal é permitir que o cliente selecione dinamicamente uma estratégia em tempo de execução. Isso proporciona uma flexibilidade significativa, pois as estratégias podem ser trocadas sem modificar o código do cliente.

Na solução, surge o momento em que o usuário faz uma solicitação ao chat, podendo escolher entre interagir por meio de voz ou texto. Quando se trata de solicitações feitas por voz, é necessário realizar a transcrição desse áudio; por outro lado, no caso de solicitações por texto, estas podem ser encaminhadas diretamente para o LLM, representando o modelo de linguagem natural. No contexto específico, as estratégias disponíveis consistem em enviar o conteúdo da solicitação para um Serviço de Transcrição de Fala (STT) ou encaminhá-lo diretamente para o LLM, dependendo do tipo de conteúdo recebido.

Além disso, para garantir uma experiência do usuário otimizada, é essencial que o solicitante confirme no chat se o entendimento do LLM está alinhado com suas intenções. Nesse cenário, outras duas estratégias podem ser empregadas. Em caso de uma confirmação positiva, o sistema pode avançar para a próxima etapa, direcionando o usuário ao objeto solicitado. Por outro lado, diante de uma confirmação negativa, seria necessário reiniciar a conversa para assegurar a compreensão correta da requisição.

Em resumo, possuímos as seguintes aplicações:

Tipo de Design Pattern | Descrição da aplicação 
---------------------- | ----------------------
Strategy Pattern       | Estratégias de formato de requisição: envio para o STT (áudio) e envio direto para o LLM (texto).
Strategy Pattern       | Estratégias de confirmação no chat: se o objeto estiver correto (o robô poderá realizar sua próxima tarefa) e se o objeto estiver incorreto (a conversa é reiniciada)
