from src.models import Base
from src.db import engine

# создаем таблицы
Base.metadata.create_all(bind=engine)