---
sidebar_position: 3
slug: '/requisitos-nao-funcionais'
---

# Requisitos Não Funcionais

<div style={{display: 'flex', gap:'50px', paddingLeft:'30px' }}>

| N° | Requisito Não Funcional |
|--------|-----------|
| 1 | O sistema deve ser capaz de mapear um espaço de 50m² em cerca de 10 minutos |
| 2 | O relatório deve ser gerado em menos de 30 segundos |
| 3 | O dashboard deve ser gerado em menos de 30 segundos |
| 4 | A lista com as peças solicitadas deve ser gerada em menos de 5 segundos |
| 5 | A resposta ao comando de voz não deve demorar mais que 5 segundos para ser executada |
| 6 | O sistema deve processar comandos de fala ou texto em menos de 5 segundos |
| 7 | O sistema deve ser capaz de operar por pelo menos 8 horas contínuas sem falhas |
| 8 | O robô deve encontrar a melhor rota para chegar nos seus destinos em menos de 20 minutos |
| 9 | O robô deve ter uma margem de segurança em suas rotas de, pelo menos, 5cm |
| 10 | O robô de serviço deve ser capaz de operar continuamente por um período mínimo de 8 horas sem necessidade de recarga, garantindo assim a cobertura de um turno de trabalho completo no almoxarifado |
</div>

## 1. Mapeamento de Espaço

- **Requisito Não Funcional (RNF):** O sistema deve ser capaz de mapear um espaço de 50m² em cerca de 10 minutos.
- **Método de Teste:**
    1. **Preparação:** Selecionar um espaço de 50m² para o teste.
    2. **Execução:** Iniciar o processo de mapeamento e cronometrar o tempo necessário para a conclusão.
    3. **Avaliação:** Verificar se o mapeamento foi concluído em 10 minutos ou menos.
    4. **Documentação:** Registrar o tempo exato de mapeamento e a qualidade do mapa gerado.

## 2. Geração de Relatório

- **Requisito Não Funcional (RNF):** O relatório deve ser gerado em menos de 30 segundos.
    
- **Método de Teste:**
    
    1. **Preparação:** Garantir que o sistema esteja operacional e pronto para gerar relatórios.
    2. **Execução:** Solicitar a geração de um relatório e cronometrar o tempo de processamento.
    3. **Avaliação:** Confirmar se o relatório foi gerado em menos de 30 segundos.
    4. **Documentação:** Anotar o tempo de geração do relatório e a integridade dos dados contidos.

## 3. Geração de Dashboard

- **Requisito Não Funcional (RNF):** O dashboard deve ser gerado em menos de 30 segundos.
    
- **Método de Teste:**
    
    1. **Preparação:** Assegurar que o sistema esteja configurado para gerar dashboards.
    2. **Execução:** Iniciar a geração do dashboard e medir o tempo necessário.
    3. **Avaliação:** Verificar se o dashboard foi gerado em menos de 30 segundos.
    4. **Documentação:** Documentar o tempo de geração e a qualidade visual e informativa do dashboard.

## 4. Geração Rápida da Lista de Peças

**Requisito Não Funcional (RNF):** A lista com as peças solicitadas pelo operador deve ser gerada pelo sistema do robô em menos de 5 segundos após a solicitação.

**Método de Teste:**

- **Execução:** Realizar múltiplas solicitações de peças ao sistema do robô.
- **Avaliação:** Medir o tempo entre a solicitação e a geração da lista de peças.
- **Critério de Aceitação:** O requisito é atendido se a lista for gerada em menos de 5 segundos em todas as solicitações.

## 5. Resposta Rápida ao Comando de Voz

**Requisito Não Funcional (RNF):** A resposta do robô ao comando de voz do operador não deve demorar mais que 5 segundos para ser executada.

**Método de Teste:**

- **Execução:** Emitir comandos de voz variados ao robô.
- **Avaliação:** Cronometrar o tempo entre o comando de voz e a execução da resposta pelo robô.
- **Critério de Aceitação:** O requisito é atendido se a resposta for executada em menos de 5 segundos em todos os comandos.

## 6. Processamento Rápido de Comandos de Fala ou Texto

**Requisito Não Funcional (RNF):** O sistema do robô deve processar comandos de fala ou texto em menos de 5 segundos.

**Método de Teste:**

- **Execução:** Enviar comandos de fala e texto ao sistema do robô.
- **Avaliação:** Medir o tempo entre o envio do comando e a resposta do sistema.
- **Critério de Aceitação:** O requisito é atendido se o processamento for concluído em menos de 5 segundos em todos os comandos.

## 7. Requisito Não Funcional: Operação Contínua

**Aspecto Específico do Sistema:** Estabilidade Operacional

**Requisito Não Funcional (RNF):** O sistema deve ser capaz de operar por pelo menos 8 horas contínuas sem falhas, garantindo a confiabilidade e a continuidade das operações no almoxarifado.

**Método de Teste**

-  **Preparação:**
   - Garantir que o sistema esteja em condições normais de operação.
   - Iniciar o teste no início de um turno de trabalho.

- **Execução:**
   - Monitorar continuamente o sistema durante 8 horas de operação.
   - Registrar qualquer falha ou interrupção que ocorra.

- **Avaliação:**
   - O requisito é considerado atendido se o sistema operar de forma contínua e sem falhas durante o período de 8 horas.

- **Documentação:**
   - Documentar os resultados do teste, incluindo qualquer falha ou interrupção observada.

## 8. Requisito Não Funcional: Eficiência de Navegação

**Aspecto Específico do Robô:** Navegação e Tempo de Resposta

**Requisito Não Funcional (RNF):** O robô deve encontrar a melhor rota para chegar aos seus destinos em menos de 20 minutos, otimizando o tempo de busca e deslocamento no almoxarifado.

**Método de Teste**

-  **Preparação:**
   - Definir diversos destinos dentro do almoxarifado.

-  **Execução:**
   - Solicitar ao robô que encontre a rota para cada destino.
   - Cronometrar o tempo que o robô leva para encontrar e percorrer a rota até o destino.

-  **Avaliação:**
   - O requisito é considerado atendido se o robô encontrar e percorrer a rota para cada destino em menos de 20 minutos.

-  **Documentação:**
   - Documentar os tempos registrados para cada rota.

## 9. Requisito Não Funcional: Margem de Segurança

**Aspecto Específico do Robô:** Segurança na Navegação

**Requisito Não Funcional (RNF):** O robô deve manter uma margem de segurança em suas rotas de, pelo menos, 5cm, evitando colisões e garantindo a segurança no ambiente de trabalho.

**Método de Teste**

- **Preparação:**
   - Configurar um percurso de teste com obstáculos.

- **Execução:**
   - Fazer o robô percorrer o trajeto, observando a distância mantida em relação aos obstáculos.

-  **Avaliação:**
   - Utilizar uma régua ou dispositivo de medição para verificar se a margem de segurança de 5cm é mantida.
   - O requisito é considerado atendido se o robô mantiver a margem de segurança em todas as situações.

-  **Documentação:**
   - Documentar as medições e observações feitas durante o teste.

## 10. **Requisito Não Funcional:** Autonomia da Bateria

**Requisito Não Funcional (RNF):** O robô de serviço deve ser capaz de operar continuamente por um período mínimo de 8 horas sem necessidade de recarga, garantindo assim a cobertura de um turno de trabalho completo no almoxarifado.

**Método de Teste**

- **Preparação:**
    - Carregar completamente a bateria do robô antes do teste.
    - Garantir que o robô esteja em condições normais de operação.

- **Execução:**
    - Iniciar o teste no início de um turno de trabalho.
    - O robô deve realizar suas funções normais de mapeamento, navegação e interação com os operadores.
    - Monitorar continuamente o nível de bateria do robô.

- **Avaliação:**
    - Registrar o tempo total de operação até que a bateria atinja um nível crítico que exija recarga.
    - O requisito é considerado atendido se o robô operar por no mínimo 8 horas contínuas.

- **Documentação:**
    - Documentar os resultados do teste, incluindo o tempo total de operação e o comportamento do robô ao atingir o nível crítico de bateria.

## Padrão de Qualidade

- **Clareza e Precisão:** Cada RNF é específico e claro, estabelecendo um limite de tempo de 5 segundos para a execução das tarefas.
- **Mensurabilidade:** Os requisitos são quantificáveis, definindo um tempo mensurável para avaliação.
- **Relevância:** Estes RNFs são relevantes para o contexto do projeto, garantindo a eficiência e a rapidez na interação com o robô.
- **Método de Teste Prático:** Os métodos de teste são práticos e realizáveis, utilizando procedimentos padrão e equipamentos disponíveis, com critérios objetivos para avaliação.