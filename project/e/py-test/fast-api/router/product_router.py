from fastapi import APIRouter
from pydantic import BaseModel

from schemas.product_schema import Product



product_api_router = APIRouter()


@product_api_router.put('/item/{id}')
async def items(id: int, product: Product):
    return {"naber": "naber", "id": id, 'product': product}
