# P1 - PARTE PRÁTICA - Flask com SQLite

# OBJETIVO DA PARTE PRÁTICA
O objetivo da primeira parte prática é desenvolver uma API com maturidade 2 na escala de Richardson. Essa escala consiste em padrões que as API's seguem para saber o quão boa está. Como foi requerido, devemos fazer uma API de nível 2, contendo os corretos verbos HTTP, URI's que tragam contexto e status HTTP para sinalizar o usuário de sua requisição.


# RODANDO A APLICAÇÃO

```bash
# Criando um env
python -m venv venv .
# Entrando na env
source/bin/activate
# Instalando dependências
python -m pip install -r requirements.txt
# Entre em src e rode o seguinte comando para rodar um servidor flask
flask --app main run
```

Essa aplicação consiste em uma API assincrona de criação de pedido, contento as seguintes informações referentes ao usuário: nome, email e descrição do pedido.

[Demonstração](https://drive.google.com/file/d/1gu-yvDFKxHVaIGqZBmA1RDDI5LBAosLD/view?usp=sharing)

