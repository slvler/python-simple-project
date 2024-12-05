from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    first_name: str
    last_name: str
    price: float
    tax: Optional[float] = None
