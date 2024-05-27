from sqlalchemy import Column, String
from src.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    nodes = Column(String)