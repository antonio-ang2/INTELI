# Aplicação 3 - CRUD de usuários com FastAPI e SQLite

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from typing import List #Por estar utilizando o Python 3.8
import sqlite3

app = FastAPI()

# Conexão com o banco de dados
def conectar_bd():
    return sqlite3.connect('tarefas.db')

# Modelo Pydantic para validação de dados
class Tarefa(BaseModel):
    nome: str
    hora: str
    local: str


class TarefaDisplay(BaseModel):
    id: int
    nome: str
    hora: str
    local: str

# Conexão CORS middleware
@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Rota para listar todos os usuários
@app.get("/tarefas", response_model=List[TarefaDisplay])
def listar_tarefas():
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = [TarefaDisplay(id=row[0], nome=row[1], hora=row[2], local=row[3]) for row in cursor.fetchall()]
    con.close()
    return tarefas

# Rota para buscar um usuário pelo id
@app.get("/tarefas/{id}", response_model=TarefaDisplay)
def buscar_tarefa(id: int):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
    tarefa = cursor.fetchone()
    con.close()
    if tarefa:
        return TarefaDisplay(id=tarefa[0], nome=tarefa[1], hora=tarefa[2], local=tarefa[3])
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para cadastrar um usuário
@app.post("/tarefas", response_model=TarefaDisplay, status_code=status.HTTP_201_CREATED)
def cadastrar_tarefa(tarefa: Tarefa):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('INSERT INTO tarefas (nome, hora, local) VALUES (?, ?, ?)', (tarefa.nome, tarefa.hora, tarefa.local))
    tarefa_id = cursor.lastrowid
    con.commit()
    con.close()
    return {**tarefa.dict(), "id": tarefa_id}

# Rota para atualizar um usuário
@app.put("/tarefas/{id}", response_model=TarefaDisplay)
def atualizar_tarefa(id: int, tarefa:Tarefa):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('UPDATE tarefas SET nome = ?, hora = ?, local = ? WHERE id = ?', (tarefa.nome, tarefa.hora, tarefa.local, id))
    if cursor.rowcount == 0:
        con.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    con.commit()
    con.close()
    return {**tarefa.dict(), "id": id}

# Rota para deletar um usuário
@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: int):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    if cursor.rowcount == 0:
        con.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    con.commit()
    con.close()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Iniciar a aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)