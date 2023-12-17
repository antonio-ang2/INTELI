# PONDERADA 6

# INFORMAÇÕES DO ALUNO
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Antonio Angelo Teixeira | Engenharia da Computação | 8 | 2


## DESCRIÇÃO DA ATIVIDADE


A oitava atividade ponderada visa a implementação de um sistema de tradução a partir de um arquivo de áudio, submetendo-o a conversão de um speech-to-text(stt) e, a partir disso, conversão desse para um text-to-speech(tts). O sistema tem um funcionamento pegando um áudio disponibilizado pelo usuário no caminho de execução do script, o que gera conversão para texto e, posteriormente, a conversão em um arquivo de áudio .wav que, por fim é reproduzido.

Dessa forma, optrei por não utilizar LLM, apenas um módulo chamado 'Translator' pertencente a biblioteca de tradução do Google. 



## COMO EXECUTAR O PROJETO
### INSTALAÇAÕ DE DEPEDÊNCIAS
Antes de executar o programa, deve-se instalar as dependências. Para isso, digite o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```


### Execução
Depois de completar a instalação, ainda no mesmo terminal execute o seguinte comando: 

```bash
python tradutor.py desabafo.wav
```

PS: Deve-se passar o caminho específico do arquivo que o usuário quer tradutor.
## FUNCIONAMENTO DO SISTEMA

O sistema tem o funcionamento baseado nas seguintes etapas:

- Carrega o arquivo de áudio disponibilizado pelo usuário;
- Converte o áudio em texto no mesmo idioma;
- Traduz o texto para o idioma destino, no caso, inglês;
- Transforma o texto em fala novamente e grava em um arquivo .wav;
- Reproduz o arquivo .wag, mostrando a tradução com um sotaque meio carregado.



# Vídeo de Demonstração

https://drive.google.com/file/d/1pVfgPvgGhHzFtPGpNbhxvnRPvalvni9Q/view?usp=sharing






