# PONDERADA 4

# INFORMAÇÕES DO ALUNO
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 8 | 2


## DESCRIÇÃO DA ATIVIDADE


A proposta da quarta atividade ponderada visa a implementação de um nó ROS que seja um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado.

Dessa forma, optei por realizar essa atividade usando o Ollama, um LLM open source desenvolvido pela Meta. O propósito central dessa atividade é desafiar o aluno a fazer seu próprio LLM, integrado a uma interface gráfica, optei pelo gradio, que carregaria localmente. O enfoque está na avaliação e aplicação dos conhecimentos em ROS2, utilizando integração com uma api de modelo pronta e importação e integração de módulos com o gradio.

# COMO EXECUTAR O PROJETO

## INSTALAÇÃO

Instalar  o Modelo Ollama:

Para instalar o modelo do chatbot na máquina, utilize o seguinte comando:

```bash
ollama create security-expert -f Modelfile
```

### INSTALAR DEPENDÊNCIAS:

Instale as dependências necessárias executando o seguinte comando:

```bash
pip install -r requirements.txt
```

### Execução
Depois de completar a instalação, execute o chatbot usando o seguinte comando:

```bash
python chat.py
```


# Vídeo de Demonstração


<video src="m8_ponderada4.mp4" controls title="Title"></video>
