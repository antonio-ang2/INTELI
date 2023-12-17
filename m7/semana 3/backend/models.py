from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = declarative_base()

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Note(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    grade = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))