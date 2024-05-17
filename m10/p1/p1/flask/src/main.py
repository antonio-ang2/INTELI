from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conect_db():
    return sqlite3.connect('orders.db')

# Resolve problema do CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


class Orders:
    def __init__(self, id, name, email, description):
        self.id = id
        self.name = name
        self.email = email
        self.description = description
    def __repr__(self) -> str:
        return f'<Pedido name:{self.name}; email:{self.email}; description:{self.description}; id:{self.id}>>'

@app.route("/orders/getall", methods=['GET'])
def get_orders():
    conect = conect_db()
    cursor = conect.cursor()
    cursor.execute('select * from orders')
    orders = cursor.fetchall()
    conect.close()
    return jsonify(orders)



@app.route("/orders/getone/<int:id>", methods=['GET'])
def get_order(id):
    conect = conect_db()
    cursor = conect.cursor()
    cursor.execute('select * from orders where id = ?', (id,))
    order = cursor.fetchone()
    conect.close()
    return jsonify(order)


@app.route('/orders/create', methods=['POST'])
def create_order():
    new_order = request.json
    conect = conect_db()
    cursor = conect.cursor()
    cursor.execute('insert into orders (name, email, description) values (?, ?, ?)', (new_order['name'], new_order['email'], new_order['description']))
    conect.commit()
    conect.close()
    return jsonify(new_order), 201


# Rota para atualizar uma tarefa
@app.route('/orders/update/<int:id>', methods=['PUT'])
def update_order(id):
    order_uploaded = request.json
    conect = conect_db()
    cursor = conect.cursor()
    cursor.execute('update orders set name = ?, email = ?, description = ?, where id = ?', (order_uploaded['name'], order_uploaded['email'], order_uploaded['description']))
    conect.commit()
    conect.close()
    return jsonify(order_uploaded)


# Rota para deletar uma tarefa
@app.route('/orders/delete/<int:id>', methods=['DELETE'])
def delete_order(id):
    conect = conect_db()
    cursor = conect.cursor()
    cursor.execute('delete from orders where id = ?', (id,))
    conect.commit()
    conect.close()
    return '', 204
