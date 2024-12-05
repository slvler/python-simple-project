# Database - Orm Katmanı
## oluşturulan classlar veritabanındaki tablolara denk gelmektedir.
from sqlalchemy import Column, Float, Integer, String
from mod.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    price = Column(Float(50))
    tax = Column(Float(50))
