from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config import Base


class User(Base):
    """ Create model User"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    status = Column(String, default="offline")

class Message(Base):
    """ Create model Message"""
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String, index=True)
    timestamp = Column(DateTime)
    read = Column(Integer, default=0)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

class PrivateMessage(Base):
    """ Create model PrivateMessage"""
    __tablename__ = 'private_messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String, index=True)
    timestamp = Column(DateTime)
    read = Column(Integer, default=0)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

class Contact(Base):
    """ Create model Contact"""
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    contact_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", foreign_keys=[user_id])
    contact = relationship("User", foreign_keys=[contact_id])

class Group(Base):
    """ Create model Group"""
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class GroupUser(Base):
    """ Create model GroupUser"""
    __tablename__ = 'group_users'
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    group = relationship("Group")
    user = relationship("User")

class GroupMessage(Base):
    """ Create model GroupMessage"""
    __tablename__ = 'group_messages'
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    sender_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String, index=True)
    timestamp = Column(DateTime)
    read = Column(Integer, default=0)

    group = relationship("Group")
    sender = relationship("User")

class Notification(Base):
    """ Create model Notification"""
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String, index=True)
    timestamp = Column(DateTime)
    read = Column(Integer, default=0)

    user = relationship("User")

class FavoriteMessage(Base):
    """ Create model FavoriteMessage"""
    __tablename__ = 'favorite_messages'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message_id = Column(Integer, ForeignKey('messages.id'))

    user = relationship("User")
    message = relationship("Message")
