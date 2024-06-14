# Aplicação 3 - CRUD de usuários com FastAPI e SQLite
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Conexão com o banco de dados
def conectar_bd():
    return sqlite3.connect('blog.db')

# Modelo Pydantic para validação de dados
class Blog(BaseModel):
    title: str
    content: str


class BlogDisplay(BaseModel):
    id: int
    title: str
    content: str

# Conexão CORS middleware
@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Rota para listar todos os usuários
@app.get("/blog", response_model=List[BlogDisplay])
def listar_posts():
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM blog')
    post = [BlogDisplay(id=row[0], title=row[1], content=row[2]) for row in cursor.fetchall()]
    con.close()
    return post

# Rota para buscar um post pelo id
@app.get("/blog/{id}", response_model=BlogDisplay)
def buscar_post(id: int):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM blog WHERE id = ?', (id,))
    post = cursor.fetchone()
    con.close()
    if post:
        return BlogDisplay(id=post[0], title=post[1], content=post[2])
    raise HTTPException(status_code=404, detail="Post não encontrado")

# Rota para cadastrar um usuário
@app.post("/blog", response_model=BlogDisplay, status_code=status.HTTP_201_CREATED)
def cadastrar_post(post: Blog):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('INSERT INTO blog (title, content) VALUES (?, ?)', (post.title, post.content))
    post_id = cursor.lastrowid
    con.commit()
    con.close()
    return {**post.dict(), "id": post_id}

# Rota para atualizar um usuário
@app.put("/blog/{id}", response_model=BlogDisplay)
def atualizar_post(id: int, post:Blog):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('UPDATE blog SET title = ?, content = ? WHERE id = ?', (post.title,post.content, id))
    if cursor.rowcount == 0:
        con.close()
        raise HTTPException(status_code=404, detail="Post não encontrado")
    con.commit()
    con.close()
    return {**post.dict(), "id": id}

# Rota para deletar um post
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_post(id: int):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute('DELETE FROM blog WHERE id = ?', (id,))
    if cursor.rowcount == 0:
        con.close()
        raise HTTPException(status_code=404, detail="Post não encontrado")
    con.commit()
    con.close()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Iniciar a aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)