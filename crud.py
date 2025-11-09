from sqlalchemy.orm import Session
from models import PrivateMessage, Contact


async def create_private_message(db: Session, sender_id: int, receiver_id: int, content: str):
    db_message = PrivateMessage(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

async def get_private_messages(db: Session, user_id: int):
    return db.query(PrivateMessage).filter(
        (PrivateMessage.sender_id == user_id) | (PrivateMessage.receiver_id == user_id)
    ).all()

async def mark_message_as_read(db: Session, message_id: int):
    db_message = db.query(PrivateMessage).filter(PrivateMessage.id == message_id).first()
    db_message.read = 1
    db.commit()
    db.refresh(db_message)
    return db_message

async def add_contact(db: Session, user_id: int, contact_id: int):
    db_contact = Contact(user_id=user_id, contact_id=contact_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

async def get_contacts(db: Session, user_id: int):
    return db.query(Contact).filter(Contact.user_id == user_id).all()

async def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    db.delete(db_contact)
    db.commit()
    return db_contact