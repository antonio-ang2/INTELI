from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import sqlite3

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Tarefas',
          description='Uma simples API de CRUD de tarefas')

ns = api.namespace('tarefas', description='Operações de Tarefas')

tarefa_model = api.model('Tarefa', {
    'id': fields.Integer(readOnly=True, description='O identificador único da tarefa'),
    'nome': fields.String(required=True, description='O nome da tarefa'),
    'hora': fields.String(required=True, description='A hora da tarefa'),
    'local': fields.String(required=True, description='O local da tarefa')
})

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

# Rota para listar todos as tarefas
@ns.route('/')
class TarefaList(Resource):
    @ns.doc('listar_tarefas')
    @ns.marshal_list_with(tarefa_model)
    def get(self):
        '''Lista todas as tarefas'''
        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute('select * from tarefas')
        tarefas = cursor.fetchall()
        con.close()
        return tarefas

    @ns.doc('cadastrar_tarefa')
    @ns.expect(tarefa_model)
    @ns.marshal_with(tarefa_model, code=201)
    def post(self):
        '''Cadastra uma nova tarefa'''
        nova_tarefa = api.payload
        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute('insert into tarefas (nome, hora, local) values (?, ?, ?)', 
                      (nova_tarefa['nome'], nova_tarefa['hora'], nova_tarefa['local']))
        con.commit()
        con.close()
        return nova_tarefa, 201

# Rota para buscar uma tarefa pelo id
@ns.route('/<int:id>')
@ns.response(404, 'Tarefa não encontrada')
@ns.param('id', 'O identificador da tarefa')
class Tarefa(Resource):
    @ns.doc('buscar_tarefa')
    @ns.marshal_with(tarefa_model)
    def get(self, id):
        '''Busca uma tarefa pelo id'''
        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute('select * from tarefas where id = ?', (id,))
        tarefa = cursor.fetchone()
        con.close()
        if tarefa:
            return tarefa
        api.abort(404)

    @ns.doc('atualizar_tarefa')
    @ns.expect(tarefa_model)
    @ns.marshal_with(tarefa_model)
    def put(self, id):
        '''Atualiza uma tarefa existente'''
        tarefa_atualizada = api.payload
        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute('update tarefas set nome = ?, hora = ?, local = ? where id = ?', 
                      (tarefa_atualizada['nome'], tarefa_atualizada['hora'], tarefa_atualizada['local'], id))
        con.commit()
        con.close()
        return tarefa_atualizada

    @ns.doc('deletar_tarefa')
    @ns.response(204, 'Tarefa deletada')
    def delete(self, id):
        '''Deleta uma tarefa'''
        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute('delete from tarefas where id = ?', (id,))
        con.commit()
        con.close()
        return '', 204

if __name__ == '__main__':
    app.run(debug=False)
