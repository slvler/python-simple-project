from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class Person(Base):
    __tablename__ = 'brands1'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"({self.id} {self.name})"



engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/test', echo=True, future=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


person = Person(2, "Test2")
session.add(person)
session.commit()