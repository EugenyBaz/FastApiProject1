from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_group, add_user_to_group, create_group_message, get_group_messages
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/group/", tags= ["Endpoints groups"])
async def create_new_group(name: str, db: Session = Depends(get_db)):
    return await create_group(db, name)

@router.post("/group/{group_id}/user/", tags= ["Endpoints groups"])
async def add_user(group_id: int, user_id: int, db: Session = Depends(get_db)):
    return await add_user_to_group(db, group_id, user_id)

@router.post("/group/{group_id}/message/", tags= ["Endpoints groups"])
async def send_group_message(group_id: int, sender_id: int, content: str, db: Session = Depends(get_db)):
    return await create_group_message(db, group_id, sender_id, content)

@router.get("/group/{group_id}/messages/", tags= ["Endpoints groups"])
async def read_group_messages(group_id: int, db: Session = Depends(get_db)):
    return await get_group_messages(db, group_id)