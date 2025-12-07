from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import set_user_status, get_user_status
from database import get_db

router = APIRouter()

@router.post("/status/", tags= ["Endpoints status"])
async def update_status(user_id: int, status: str, db: Session = Depends(get_db)):
    """ Ручка обновления статуса"""
    return await set_user_status(db, user_id, status)

@router.get("/status/{user_id}", tags= ["Endpoints status"])
async def read_status(user_id: int, db: Session = Depends(get_db)):
    """ Ручка отображения текущего статуса пользователя"""
    return await get_user_status(db, user_id)