from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import add_favorite_message, get_favorite_messages, delete_favorite_message
from database import get_db

router = APIRouter()

@router.post("/favorite/", tags= ["Endpoints favorites"])
async def create_favorite(user_id: int, message_id: int, db: Session = Depends(get_db)):
    """ Ручка создания избранного сообщения """
    return await add_favorite_message(db, user_id, message_id)

@router.get("/favorites/{user_id}", tags= ["Endpoints favorites"])
async def read_favorites(user_id: int, db: Session = Depends(get_db)):
    """ Ручка просмотра избранного сообщения """
    return await get_favorite_messages(db, user_id)

@router.delete("/favorite/{favorite_id}", tags= ["Endpoints favorites"])
async def remove_favorite(favorite_id: int, db: Session = Depends(get_db)):
    """ Ручка удаления избранного сообщения """
    return await delete_favorite_message(db, favorite_id)