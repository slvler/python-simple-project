from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(25), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders=relationship('Order',back_populates='user')



class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user=relationship('User',back_populates='orders')
