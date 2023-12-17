# ATIVIDADE PONDERADA 1

## 1. Objetivo
Desenvolver a habilidade de definir requisitos não funcionais (RNFs) e criar 
métodos de teste para validar esses requisitos em um contexto prático.

## 2. Enunciado

Desenvolva um requisito não funcional (RNF) para um robô de serviço utilizado 
no contexto do projeto deste módulo. O problema proposto se divide em:

1. **Definição do Requisito Não Funcional**

   - Escolha um aspecto específico do robô (por exemplo, autonomia da bateria,
velocidade de movimento, capacidade de interação com os hóspedes, etc.).
   - Defina um requisito não funcional claro e mensurável para esse aspecto. 

2. **Método de Teste**

   - Descreva uma forma de testar o requisito não funcional que você definiu. O
método de teste deve ser prático e fornecer resultados quantitativos ou
qualitativos claros.

## 3. Padrão de Qualidade para a Entrega

1. **Clareza e Precisão:** O requisito não funcional definido deve ser claro,
específico e livre de ambiguidades. Deve ser facilmente compreendido por
qualquer pessoa familiarizada com o contexto.

2. **Mensurabilidade:** O RNF deve ser quantificável. Por exemplo, em vez de
dizer "o robô deve mover-se rapidamente", especifique "o robô deve ser capaz de
se mover a uma velocidade de 5 km/h".

3. **Relevância:** O RNF escolhido deve ser relevante para o contexto do 
projeto a ser desenvolvido no decorrer do módulo 8.

4. **Método de Teste Prático:** O método de teste proposto deve ser realizável
com os recursos e tecnologias disponíveis. Deve ser descrito em etapas claras e
fornecer critérios objetivos para determinar se o RNF foi atendido.

5. **Apresentação:** A entrega deve ser bem organizada, com uma estrutura lógica
e linguagem clara. Erros gramaticais e ortográficos devem ser minimizados. O 
resultado final deve ser integrado à documentação do grupo.

6. **Originalidade:** A resposta deve ser original e refletir o pensamento
independente do aluno. Respostas pouco originais serão penalizadas. Respostas 
copiadas serão consideradas plágio.

7. **Coesão:** O RNF e método de validação devem manter a coesão dentro da 
documentação do grupo. O método de apresentação e estilo de escrita não podem 
ser diferentes entre os RNFs descritos.

## 4. Entrega 

A entrega da atividade deverá ser feita em dois ambientes:

1. **Card da Adalove:** O card da adalove deverá ser preenchido com a sua 
resposta.
2. **Documentação do grupo:** O RNF desenvolvido deve estar na documentação do 
grupo.


## RESPOSTA:

Os requisitos não funcionais representam as características que o projeto deve atender em termos de desempenho, usabilidade, confiabilidade, segurança, disponibilidade, manutenção e tecnologias envolvidas. Um requisito não funcional proposto pelo grupo é que "O relatório deve ser gerado em menos de 30 segundos". Este requisito se refere à funcionalidade de desempenho da aplicação e pode ser testado gerando relatórios com diferentes tamanhos de arquivo.

Para testar esse requisito, durante a fase de testes da aplicação, podemos iniciar gerando um relatório com 10 requisições de peças, incluindo informações como nome do requisitante, nome das peças, quantidade e data. Após passar nesse primeiro teste com 10 requisições, podemos aumentar a carga de trabalho, acumulando mais requisições e testando se o sistema ainda é capaz de gerar o relatório em 30 segundos, mesmo com 100 requisições. Podemos continuar aumentando a carga de trabalho até atingir, por exemplo, 1000 requisições, para garantir que o sistema seja escalável.

Eu assumi a responsabilidade direta por este requisito não funcional, e estou encarregado de projetar a arquitetura deste módulo. Se o sistema não cumprir esse requisito não funcional, isso poderá indicar que a arquitetura precisa ser revisada e aprimorada.
