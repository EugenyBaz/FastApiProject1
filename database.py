from config import database, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv(override=True)

engine = create_engine(f"postgresql+psycopg2://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}@{os.getenv('HOST_DB')}/{os.getenv('NAME_DB')}")
SessionLocal = sessionmaker(bind=engine)

async def init_db():
    async with database:
        await database.connect()


def create_tables():
    Base.metadata.create_all(bind=engine)