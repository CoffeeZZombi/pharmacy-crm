from pydantic import BaseModel
from datetime import date

class ItemBase(BaseModel):
    name: str
    manufacturer: str
    purchase_price: float
    sale_price: float
    stock_quantity: int
    category: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        from_attributes = True