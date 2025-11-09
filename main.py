from contextlib import asynccontextmanager
from database import database, create_tables, init_db
from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app: FastAPI):

    create_tables()
    await init_db()

    # выполняется при старте
    await database.connect()
    print("Database connected")

    yield

    # выполняется при остановке
    await database.disconnect()
    print("Database disconnected")


# создаем экземпляр приложения
app = FastAPI(lifespan=lifespan)

# создаем простой эндпоинт, который возвращает приветственное сообщение
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}



@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello, {name}!"}