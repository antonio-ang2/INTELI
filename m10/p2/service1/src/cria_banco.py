import sqlite3

# Conectar ao banco de dados SQLite, ou criar se não existir
conn = sqlite3.connect('blog.db')

# Criar um objeto cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela com as colunas especificadas
cursor.execute('''
CREATE TABLE IF NOT EXISTS blog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')

# Commit as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Tabela 'blog' criada com sucesso.")
