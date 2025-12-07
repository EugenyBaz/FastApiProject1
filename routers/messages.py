from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_private_message, get_private_messages, mark_message_as_read
from database import get_db

router = APIRouter()

@router.post("/private_message/", tags= ["Endpoints messages"])
async def send_private_message(sender_id: int, receiver_id: int, content: str, db: Session = Depends(get_db)):
    """ Ручка создание приватного сообщения"""
    return await create_private_message(db, sender_id, receiver_id, content)

@router.get("/private_message/", tags= ["Endpoints messages"])
async def read_private_messages(user_id: int, db: Session = Depends(get_db)):
    """ Ручка просмотра приватного сообщения"""
    return await get_private_messages(db, user_id)

@router.post("/private_message/read/", tags= ["Endpoints messages"])
async def mark_as_read(message_id: int, db: Session = Depends(get_db)):
    """ Ручка пометки как прочитанного приватного сообщения"""
    return await mark_message_as_read(db, message_id)