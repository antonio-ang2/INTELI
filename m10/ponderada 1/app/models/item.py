from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Cria a base para os modelos
Base = declarative_base()

#Define a tabela base
class Todo(Base):
    """
    Classe que representa a tabela de atividades para realizar do sistema
    """
    __tablename__ = "Todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, subject={self.subject}, time={self.time}>"