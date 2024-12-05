# Database - Orm Katmanı
## oluşturulan classlar veritabanındaki tablolara denk gelmektedir.
from sqlalchemy import Column, Integer, String
from mod.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
