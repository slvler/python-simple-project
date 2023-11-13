from fastapi import APIRouter

order_routes = APIRouter(
    prefix='/order',
    tags=['order']
)

@order_routes.get('/all')
def list():
    return "hello order"


@order_routes.get('/show')
def show():
    return "hello order"