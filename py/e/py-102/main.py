import uvicorn
from fastapi import FastAPI, Depends, status
from typing import Optional, Annotated


from schemas.category import CategoryBase
from schemas.product import ProductBase
from schemas.user import UserBase

from mod.category import Category
from mod.product import Product
from mod.user import User

from mod.database import Base

from mod.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/')
def index():
    return {"data": {'name': 'joe'}}


## path parameters
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'data'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{slug}/comments')
def comments(slug):
    return {"data": {'slug': slug}}


## query parameters

@app.get('/city')
async def city(city):
    return {'data': f'{city} is small'}


@app.get('/teams')
async def teams(team, order: bool):
    if order:
        return {'data': f'{team} is big'}
    else:
        return {'data': f'{team} is small'}


@app.get('/animals')
async def teams(limit: int = 10, order: bool = True, sort: Optional[str] = None):
    if order:
        return {'data': f'{limit} is big'}
    else:
        return {'data': f'{limit} is small'}




### product section
@app.post('/product/store', status_code=status.HTTP_201_CREATED)
def product_store(product: ProductBase, db: db_dependency):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    return {'data': 'store', 'product': product}


### user section
@app.get('/user/list')
def user_list(db: db_dependency):
    return db.query(User).all()


@app.get('/user/show/{user_id}')
def user_show(user_id, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return {'data': 'user not found'}
    else:
        return user


@app.post('/user/store', status_code=status.HTTP_201_CREATED)
def user_store(user: UserBase, db: db_dependency):
    try:
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        return {'data': user}
    except:
        return {'data': 'fail'}


@app.put('/user/edit/{user_id}')
def user_edit(user_id: int, user: UserBase, db: db_dependency):
    user_record = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        user_record.username = user.username
        db.commit()
        return {'data': 'Successful'}
    else:
        return {'data': 'Fail'}

@app.delete('/user/delete/{user_id}')
def user_edit(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        db.delete(user)
        db.commit()
        return {'data': 'Successful'}
    else:
        return {'data': 'USER NOT FOUND'}



### category section
@app.post('/category/store', status_code=status.HTTP_201_CREATED)
def category_store(category: CategoryBase, db: db_dependency):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    return {'data': category}




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
