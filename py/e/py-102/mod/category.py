# Database - Orm Katmanı
## oluşturulan classlar veritabanındaki tablolara denk gelmektedir.
from sqlalchemy import Column, Integer, String
from mod.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(50))
    tag = Column(String(50))