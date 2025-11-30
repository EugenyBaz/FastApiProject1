from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_private_message, get_private_messages, mark_message_as_read
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/private_message/", tags= ["Endpoints messages"])
async def send_private_message(sender_id: int, receiver_id: int, content: str, db: Session = Depends(get_db)):
    return await create_private_message(db, sender_id, receiver_id, content)

@router.get("/private_message/", tags= ["Endpoints messages"])
async def read_private_messages(user_id: int, db: Session = Depends(get_db)):
    return await get_private_messages(db, user_id)

@router.post("/private_message/read/", tags= ["Endpoints messages"])
async def mark_as_read(message_id: int, db: Session = Depends(get_db)):
    return await mark_message_as_read(db, message_id)