# PONDERADA 1 - CRUD de tarefas com Flask e SQLite e Servidor de produção

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Cria a o conector com o banco de dados
def conectar_bd():
    return sqlite3.connect('tarefas.db')

# Resolve problema do CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Cria uma entidade para as tarefas
class Tarefa:
    def __init__(self, id, nome, hora, local):
        self.id = id
        self.nome = nome
        self.hora = hora
        self.local = local
    def __repr__(self):
        return f'<Tarefa nome:{self.nome}; hora:{self.hora}; local:{self.local}; id:{self.id}>'

# Rota para listar todos as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('select * from tarefas')
    tarefas = cursor.fetchall()
    con.close()
    return jsonify(tarefas)

# Rota para buscar uma tarefa pelo id
@app.route('/tarefas/<int:id>', methods=['GET'])
def buscar_tarefa(id):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('select * from tarefas where id = ?', (id,))
    tarefa = cursor.fetchone()
    con.close()
    return jsonify(tarefa)

# Rota para cadastrar uma tarefa
@app.route('/tarefas', methods=['POST'])
def cadastrar_tarefa():
    nova_tarefa = request.json
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('insert into tarefas (nome, hora, local) values (?, ?, ?)', (nova_tarefa['nome'], nova_tarefa['hora'], nova_tarefa['local'] ))
    con.commit()
    con.close()
    return jsonify(nova_tarefa), 201

# Rota para atualizar uma tarefa
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa_atualizada = request.json
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('update tarefas set nome = ?, hora = ?, local = ?, where id = ?', (tarefa_atualizada['nome'], tarefa_atualizada['hora'], tarefa_atualizada['local']))
    con.commit()
    con.close()
    return jsonify(tarefa_atualizada)

# Rota para deletar uma tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('delete from tarefas where id = ?', (id,))
    con.commit()
    con.close()
    return '', 204

if __name__ == '__main__':
    # O Guvicorn é um servidor de produção para o Flask, ele será lançado pelo container
    app.run(debug=False)