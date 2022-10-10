from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine("mysql+pymysql://root:obelix@localhost/todos_db")

Base = declarative_base()

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True, autoincrement=True)
    texto = Column(String(200))

    def as_json(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()


def get_todos():
    return session.query(Todos).all()
    
def get_todo(id):
    return session.query(Todos).filter(Todos.id == id)[0]

def add_todo(texto):
    todo = Todos(texto=texto)
    session.add(todo)
    return todo

def update_todo(id, texto):
    todo = get_todo(id)
    todo.texto = texto
    return todo

def delete_todo(id):
    todo = get_todo(id)
    session.delete(todo)

def commit():
    session.commit()

def rollback():
    session.rollback()
