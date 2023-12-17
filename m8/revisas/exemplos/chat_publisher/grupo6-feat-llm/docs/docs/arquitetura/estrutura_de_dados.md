---
sidebar_position: 4
slug: '/estrutura_de_dados'
---

# Estrutura de dados

A escolha adequada de estruturas de dados e padrões de design desempenha um papel crítico na arquitetura de software, sendo de extrema importância para o projeto. Esses elementos são fundamentais porque influenciam vários aspectos chave do desenvolvimento de software, contribuindo para a eficiência, manutenibilidade, escalabilidade e reusabilidade do sistema.

No contexto deste projeto, é essencial considerar como o robô interage com o ambiente e com os comandos recebidos (por voz ou texto, STT ou TTS) que serão processados e transformados em ações que orientam o robô até o local especificado no comando. Dessa maneira, para gerenciar esses comandos e garantir a ordem de execução, uma fila de comandos (fila) pode ser empregada. 

Os pedidos do sistema, como informações sobre a localização das peças vão ser mantidos em um dicionário que correlaciona palavras-chave com pontos no espaço do almoxarifado, por exemplo {”ponto 1”: (0, 0, 0)}, permitindo que o robô traduza comandos de textos em coordenadas espaciais e aja de acordo com a solicitação. 

Para armazenar informações de forma estruturada, como registros de operações diárias ou informações sobre peças em estoque, achamos apropriado utilizar documentos JSON (documentos que podem conter informações detalhadas sobre as operações, o inventário e o estado do almoxarifado). 

Acreditamos que o registro de todas as ações realizadas é um aspecto de extrema importância, para isso optamos por gravar um log de todas as ações em formato CSV ou em um banco de dados (db), tendo que levar em consideração a complexidade das informações a serem registradas e necessidades de consulta e relatórios futuros. Ademais, os relatórios resultantes das operações vão ser armazenados em um formato CSV, que é adequado para análise posterior.