from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_notification, get_notifications, mark_notification_as_read
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notification/")
async def send_notification(user_id: int, message: str, db: Session = Depends(get_db)):
    return await create_notification(db, user_id, message)

@router.get("/notifications/{user_id}")
async def read_notifications(user_id: int, db: Session = Depends(get_db)):
    return await get_notifications(db, user_id)

@router.post("/notification/read/")
async def mark_as_read(notification_id: int, db: Session = Depends(get_db)):
    return await mark_notification_as_read(db, notification_id)