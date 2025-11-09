from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv(override=True)

DATABASE_URL = f"postgresql+asyncpg://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}@{os.getenv('HOST_DB')}/{os.getenv('NAME_DB')}"

# Движок для асинхронного использования
database = Database(DATABASE_URL)

# Создание базового класса для всех моделей
Base= declarative_base()

