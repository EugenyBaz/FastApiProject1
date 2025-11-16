from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import add_favorite_message, get_favorite_messages, delete_favorite_message
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/favorite/")
async def create_favorite(user_id: int, message_id: int, db: Session = Depends(get_db)):
    return await add_favorite_message(db, user_id, message_id)

@router.get("/favorites/{user_id}")
async def read_favorites(user_id: int, db: Session = Depends(get_db)):
    return await get_favorite_messages(db, user_id)

@router.delete("/favorite/{favorite_id}")
async def remove_favorite(favorite_id: int, db: Session = Depends(get_db)):
    return await delete_favorite_message(db, favorite_id)