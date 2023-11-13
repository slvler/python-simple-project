from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional, Annotated
from database import SessionLocal
from sqlalchemy.orm import Session
from schemas import SingupModel
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = APIRouter(
    prefix='/auth',
    tags=['auth']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@auth_routes.post('sing_up')
def sing_up(request: SingupModel, db: db_dependency):
    db_user = db.query(User).filter(request.email == User.email).first()
    if db_user is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with already')

    new_user = User(
        username=request.username,
        email=request.email,
        password=generate_password_hash(request.password),
        is_staff=request.is_staff,
        is_active=request.is_active
    )

    db.add(new_user)
    db.commit()
    return {"data": 'succesfull', 'news_user': new_user}


@auth_routes.get('/all')
def list():
    return "hello world"


@auth_routes.get('/show')
def show():
    return "hello world"
