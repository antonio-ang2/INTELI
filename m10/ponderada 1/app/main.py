from fastapi import FastAPI, Body
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.models.item import Base, Todo

# Constantes
DB_USER = "admin"
DB_PASSWORD = "postgres"
DB_HOST = "172.17.0.2"
DB_PORT = "5432"
DB_NAME = "banco-app"

# Cria a engine de dados para o postgres
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Cria uma seção no banco
session = Session(engine)

# Cria a tabela no banco se ela já não existir
Base.metadata.create_all(engine, checkfirst=True)

app = FastAPI()

@app.get("/get_items")
def get_items():
    item = session.query(Todo).all()
    return {"data":item}

@app.get("/get_item/{id}")
def get_item(id: int):
    item = session.query(Todo).filter(Todo.id == id).first()
    return {"data":item}

@app.post("/create_item")
def create_item(data: dict = Body()):
    item = Todo(name = data['name'], subject = data['subject'], time = data['time'])
    session.add(item)
    session.commit()
    return {"data": "Item criado com sucesso!"}

@app.put("/update_item")
def update_item(data: dict = Body()):
    item = session.query(Todo).filter(Todo.id == data['id']).first()
    item.name = data['name']
    item.subject = data['subject']
    item.time = data['time']
    session.commit()
    return {"data": "Item atualizado com sucesso!"}

@app.delete("/delete_item")
def delete_item(data: dict = Body()):
    item = session.query(Todo).filter(Todo.id == data['id']).first()
    session.delete(item)
    session.commit()
    return {"data": "Item deletado com sucesso!"}
