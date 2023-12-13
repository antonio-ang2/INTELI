# PONDERADA 5

# INFORMAÇÕES DO ALUNO
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 8 | 2


## DESCRIÇÃO DA ATIVIDADE


A proposta da quainta atividade ponderada visa a implementação de um nó ROS que seja um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais, porém, dessa vez consultando um pdf com instruções desse tipo. O sistema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado.

Dessa forma, optei por realizar essa atividade usando Lnagchain com ChatGPT 3.5 e PyPDF, função para consultar pdf's pré-definidos. O propósito central dessa atividade é desafiar o aluno a fazer uma API LLM que faça consultas, integrado a uma interface gráfica, que carrega localmente. O enfoque está na avaliação e aplicação dos conhecimentos em Langchain, utilizando integração com uma api de modelo pronta e importação e integração de módulos com o gradio para construção da interface gráfica.

# COMO EXECUTAR O PROJETO

### INSTALAR DEPENDÊNCIAS:

Instale as dependências necessárias executando o seguinte comando:

```bash
pip install -r requirements.txt
```

### Execução
Depois de completar a instalação, abra três terminais diferentes e execute em cada um deles em ordem:

```bash
python input.py
```
```bash
python llm.py
```

```bash
python output.py
```


# Vídeo de Demonstração

https://drive.google.com/file/d/1Cv5sV4IdTvstYkiZXbXEHNBBT5uTCEXi/view?usp=drive_link
