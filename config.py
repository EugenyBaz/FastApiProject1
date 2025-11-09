from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://username:password@localhost/messenger_db"

# Создание движка для подключения к базе данных
engine = create_engine("sqlite://example.db")
metadata = MetaData()

# Движок для асинхронного использования
database = Database(DATABASE_URL)

# Создание базового класса для всех моделей
Base= declarative_base()

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)