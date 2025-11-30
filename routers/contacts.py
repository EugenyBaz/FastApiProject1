from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import add_contact, get_contacts, delete_contact
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/contact/", tags= ["Endpoints contacts"])
async def create_contact(user_id: int, contact_id: int, db: Session = Depends(get_db)):
    return await add_contact(db, user_id, contact_id)

@router.get("/contacts/", tags= ["Endpoints contacts"])
async def read_contacts(user_id: int, db: Session = Depends(get_db)):
    return await get_contacts(db, user_id)

@router.delete("/contact/{contact_id}", tags= ["Endpoints contacts"])
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    return await delete_contact(db, contact_id)