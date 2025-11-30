from contextlib import asynccontextmanager
from database import database, create_tables, init_db
from fastapi import FastAPI

from routers import status
from routers.users import router as users_router
from routers.profile import router as profile_router
from routers.notifications import router as notifications_router
from routers.messages import router as messages_router
from routers.groups import router as groups_router
from routers.favorites import router as favorites_router
from routers.contacts import router as contacts_router


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
app.include_router(users_router)
app.include_router(status.router)
app.include_router(profile_router)
app.include_router(notifications_router)
app.include_router(messages_router)
app.include_router(groups_router)
app.include_router(favorites_router)
app.include_router(contacts_router)

# создаем простой эндпоинт, который возвращает приветственное сообщение
@app.get("/", tags= ["Endpoints main"])
def read_root():
    return {"message": "Hello, World!"}



@app.get("/hello/{name}", tags= ["Endpoints main"])
def read_hello(name: str):
    return {"message": f"Hello, {name}!"}