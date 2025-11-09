from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_user, update_user_profile
from config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/profile/{user_id}")
async def read_profile(user_id: int, db: Session = Depends(get_db)):
    return await get_user(db, user_id)

@router.put("/profile/{user_id}")
async def update_profile(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    return await update_user_profile(db, user_id, name, email)