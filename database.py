from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

# Создание движка для подключения к базе данных
engine = create_engine("sqlite://example.db")
metadata = MetaData()

# Движок для асинхронного использования
database = Database(DATABASE_URL)

# Создание базового класса для всех моделей
Base= declarative_base()

async def init_db():
    async with database:
        await database.connect()


def create_tables():
    Base.metadata.create_all(bind=engine)