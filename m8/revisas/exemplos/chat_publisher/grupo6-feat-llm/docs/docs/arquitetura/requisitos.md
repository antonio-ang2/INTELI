---
sidebar_position: 2
slug: '/requisitos'
---



# Requisitos Funcionais

<div style={{display: 'flex', gap:'50px', paddingLeft:'30px' }}>

| N° | Requisito Funcional |
|--------|-----------|
| 1 | Mapeamento da área (espaço do almoxarifado) |
| 2 | Geração de um relatório |
| 3 | Dashboard para visualização do relatório |
| 4 | Capacidade do sistema compreender fala ou texto |
| 5 | Navegação autônoma |
| 6 | Conversão de Texto-Fala e Fala-Texto (TTS e STT) |
| 7 | Capacidade de acompanhar o robô remotamente |
| 8 | Deve haver uma confirmação para as peças que o robô sugerir |
| 9 | Deve haver uma lista com as peças que o cliente solicitou |
| 10 | O sistema deve saber quais peças existem no inventário |
| 11 | O robô deve se mover de forma segura |

</div>

## 1. Mapeamento da Área (Espaço do Almoxarifado)

**Descrição:** O robô deve ser capaz de realizar o mapeamento completo do espaço do almoxarifado, identificando a localização de todas as estantes e áreas de armazenamento.

**Critérios de Aceitação:**

- O robô deve percorrer todo o espaço do almoxarifado.
- O sistema deve criar um mapa detalhado, incluindo a localização de estantes e áreas específicas.
- O mapa deve ser preciso e atualizado conforme mudanças no layout do almoxarifado.

## 2. Geração de um Relatório

**Descrição:** O sistema deve ser capaz de gerar um relatório diário em formato CSV, contendo todas as operações realizadas pelo robô, incluindo pedidos atendidos e localizações visitadas.

**Critérios de Aceitação:**

- O relatório deve ser gerado automaticamente ao final de cada dia de operação.
- O formato do relatório deve ser CSV, facilitando a integração com outros sistemas.
- O relatório deve incluir detalhes como data, hora, pedido atendido e localização visitada.

## 3. Dashboard para Visualização do Relatório

**Descrição:** Deve haver um dashboard intuitivo para a visualização dos relatórios gerados, permitindo aos gestores acompanhar as atividades do robô e analisar dados relevantes.

**Critérios de Aceitação:**

- O dashboard deve ser acessível através de uma interface web ou aplicativo.
- Deve permitir a visualização de relatórios diários, semanais e mensais.
- O dashboard deve apresentar informações de forma clara e organizada, incluindo gráficos e tabelas quando apropriado.
- Deve haver opções para filtrar e buscar informações específicas dentro dos relatórios.

## 4. Capacidade do Sistema Compreender Fala ou Texto

- **Descrição:** O sistema deve ser capaz de compreender comandos de voz e texto em linguagem natural, permitindo que os operadores interajam com o robô utilizando fala ou texto escrito.
- **Critérios de Aceitação:**
  - O sistema deve reconhecer e interpretar comandos de voz em português com uma precisão de pelo menos 95%.
  - O sistema deve ser capaz de processar e responder a comandos de texto em português com uma precisão de pelo menos 98%.
  - O tempo de resposta do sistema para comandos de voz ou texto não deve exceder 3 segundos.

## 5. Navegação Autônoma

- **Descrição:** O robô deve ser capaz de navegar autonomamente pelo almoxarifado, evitando obstáculos e seguindo rotas otimizadas para alcançar os locais designados.
- **Critérios de Aceitação:**
  - O robô deve ser capaz de mapear o ambiente do almoxarifado e atualizar seu mapa em tempo real.
  - O robô deve evitar obstáculos com uma taxa de sucesso de pelo menos 99%.
  - O robô deve ser capaz de seguir rotas otimizadas para os locais designados, com um desvio máximo de 5% da rota ideal.

## 6. Conversão de Texto-Fala e Fala-Texto (TTS e STT)

- **Descrição:** O sistema deve ser capaz de converter texto em fala (TTS) e fala em texto (STT), permitindo uma comunicação bidirecional eficaz entre o operador e o robô.
- **Critérios de Aceitação:**
  - A conversão de texto em fala (TTS) deve ser clara e compreensível, com uma taxa de inteligibilidade de pelo menos 95%.
  - A conversão de fala em texto (STT) deve ter uma precisão de pelo menos 95% na transcrição de comandos de voz.
  - O sistema deve ser capaz de realizar a conversão TTS e STT em tempo real, com um tempo de resposta não superior a 2 segundos.

## 7. Capacidade de Acompanhar o Robô Remotamente

**Descrição:** O sistema deve permitir que os operadores ou supervisores acompanhem a localização e o status do robô em tempo real através de uma interface remota, como um aplicativo móvel ou um painel de controle baseado na web.

**Critérios de Aceitação:**

- A interface remota deve mostrar a localização atual do robô no mapa do almoxarifado.
- Deve exibir informações sobre o status do robô, incluindo nível de bateria e tarefas em andamento.
- A atualização das informações na interface remota deve ocorrer em tempo real ou com um atraso máximo de 5 segundos.

## 8. Deve Haver uma Confirmação para as Peças que o Robô Sugerir

**Descrição:** Quando o robô identificar e sugerir uma peça com base no pedido do operador, deve haver um mecanismo de confirmação para que o operador possa validar a escolha antes de prosseguir.

**Critérios de Aceitação:**

- Após sugerir uma peça, o robô deve solicitar uma confirmação do operador.
- O operador deve poder confirmar ou rejeitar a sugestão através de um comando de voz ou interface de toque.
- Se a sugestão for rejeitada, o robô deve ser capaz de oferecer alternativas ou solicitar mais informações.

## 9. Deve Haver uma Lista com as Peças que o Cliente Solicitou

**Descrição:** O sistema deve ser capaz de gerar e manter uma lista das peças solicitadas pelo operador durante a interação com o robô, facilitando o rastreamento e a gestão do pedido.

**Critérios de Aceitação:**

- A lista deve ser gerada automaticamente à medida que o operador solicita peças.
- A lista deve ser acessível tanto pelo operador quanto pelo robô durante a interação.
- A lista deve ser atualizável, permitindo adicionar ou remover itens conforme necessário.
- Após a conclusão do pedido, a lista deve ser armazenada para referência futura e integração com outros sistemas de gestão de almoxarifado.

## 10. Conhecimento do Inventário pelo Sistema

**Descrição:** O sistema deve ter a capacidade de identificar e manter um registro atualizado de todas as peças disponíveis no inventário do almoxarifado.

**Critérios de Aceitação:**

- O sistema deve ser capaz de listar todas as peças disponíveis no inventário.
- Deve haver uma funcionalidade para atualizar o inventário sempre que uma peça for adicionada ou removida.
- O sistema deve fornecer informações detalhadas sobre cada peça, incluindo nome, código, localização e quantidade disponível.

## 11. Movimento Seguro do Robô

**Descrição:** O robô deve ser capaz de se mover pelo almoxarifado de forma segura, evitando colisões com objetos, estruturas e pessoas.

**Critérios de Aceitação:**

- O robô deve ser equipado com sensores de proximidade e sistemas de detecção de obstáculos.
- Durante o movimento, o robô deve manter uma distância segura de objetos, estruturas e pessoas.
- Em caso de detecção de obstáculo iminente, o robô deve ser capaz de parar imediatamente ou desviar de forma segura.
- O robô deve seguir um caminho pré-definido, ajustando sua trajetória conforme necessário para garantir a segurança.
