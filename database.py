from config import database, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv(override=True)


#Connection to database
engine = create_engine(f"postgresql+psycopg2://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}@{os.getenv('HOST_DB')}/{os.getenv('NAME_DB')}")
SessionLocal = sessionmaker(bind=engine)

async def init_db():
    """ Инициализация базы данных"""
    async with database:
        await database.connect()


def create_tables():
    """Создание таблиц"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Создаёт сессию подключения к базе данных и корректно закрывает её после использования."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()