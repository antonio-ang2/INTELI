import sqlite3 
conectar = sqlite3.connect('orders.db')

cursor = conectar.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    description TEXT NOT NULL
)
''')

conectar.commit()

conectar.close()

print('tabela orders criada com sucesso')