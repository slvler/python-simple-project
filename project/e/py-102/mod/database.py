# Database bağlantı katmanı
## sqlalchemy ile bağlantı oluşturulur.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:DhGX/_(8C9/WmCLV@127.0.0.1:3308/fastapi'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()