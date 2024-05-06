# Aplicação 02 - Flask com SQLite e Gunicorn

O objetivo de todas as aplicações é o mesmo, prover uma solução que implementa um CRUD para usuários. A entidade usuário é composta por um identificador único (gerado pelo banco), um nome e um e-mail. A aplicação deve permitir a criação, leitura, atualização e remoção de usuários.

Será possível atualizar o nome e o e-mail do usuário. O identificador único não poderá ser alterado.

A aplicação 01 foi desenvolvida utilizando Flask e SQLite.

Para executar o projeto, siga os passos abaixo:

```bash
# Criando a imagem com Docker
docker build -t ponderada1sync .
# Executando a imagem e excluindo o container após a execução
docker run --rm -p 8000:8000 ponderada1sync
```

Essa aplicação em essencia é igual a primeira, mas com a diferença que agora estamos utilizando um servidor de produção, o Gunicorn.