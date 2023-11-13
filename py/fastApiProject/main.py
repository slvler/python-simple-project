from fastapi import FastAPI
from auth_routes import auth_routes
from order_routes import order_routes

app = FastAPI()

app.include_router(auth_routes)
app.include_router(order_routes)