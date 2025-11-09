from sqlalchemy.orm import Session
from models import PrivateMessage, Contact, Group, GroupUser, GroupMessage, User, Notification, FavoriteMessage


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

async def create_group(db: Session, name: str):
    db_group = Group(name=name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

async def add_user_to_group(db: Session, group_id: int, user_id: int):
    db_group_user = GroupUser(group_id=group_id, user_id=user_id)
    db.add(db_group_user)
    db.commit()
    db.refresh(db_group_user)
    return db_group_user

async def create_group_message(db: Session, group_id: int, sender_id: int, content: str):
    db_group_message = GroupMessage(group_id=group_id, sender_id=sender_id, content=content)
    db.add(db_group_message)
    db.commit()
    db.refresh(db_group_message)
    return db_group_message

async def get_group_messages(db: Session, group_id: int):
    return db.query(GroupMessage).filter(GroupMessage.group_id == group_id).all()

async def set_user_status(db: Session, user_id: int, status: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.status = status
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_user_status(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    return db_user.status

async def create_notification(db: Session, user_id: int, message: str):
    db_notification = Notification(user_id=user_id, message=message)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

async def get_notifications(db: Session, user_id: int):
    return db.query(Notification).filter(Notification.user_id == user_id).all()

async def mark_notification_as_read(db: Session, notification_id: int):
    db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
    db_notification.read = 1
    db.commit()
    db.refresh(db_notification)
    return db_notification

async def add_favorite_message(db: Session, user_id: int, message_id: int):
    db_favorite = FavoriteMessage(user_id=user_id, message_id=message_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

async def get_favorite_messages(db: Session, user_id: int):
    return db.query(FavoriteMessage).filter(FavoriteMessage.user_id == user_id).all()

async def get_favorite_message(db: Session, favorite_id: int):
    return db.query(FavoriteMessage).filter(FavoriteMessage.id == favorite_id).first()

async def delete_favorite_message(db: Session, favorite_id: int):
    db_favorite = db.query(FavoriteMessage).filter(FavoriteMessage.id == favorite_id).first()
    db.delete(db_favorite)
    db.commit()
    return db_favorite