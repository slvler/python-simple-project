from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str
    content: str
    tag: str
