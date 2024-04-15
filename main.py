import uuid
from sqlalchemy.dialects.postgresql import UUID
from fastapi import FastAPI, Body, status
# from fastapi.responses import
from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base
import uvicorn
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic import BaseModel


# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

# создание движка (многопоточка)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    nodes = Column(String)


# создаем таблицы
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# tom = User(id=str(uuid.uuid4()), nodes="gftfvh")
# db.add(tom)
# db.commit()

class Scheme(BaseModel):
    nodes: str

class Response(BaseModel):
    status: int


app = FastAPI()

@app.get("/fetch/{node_id}")
def fetch(node_id: str):
    tom = db.query(User).filter(User.id == node_id).first()
    return tom.nodes


@app.post("/save")
def save(scheme: Scheme) -> Response:
    response = Response(status=404)
    tom = User(id=str(uuid.uuid4()), nodes=scheme.nodes)
    db.add(tom)
    db.commit()
    return response