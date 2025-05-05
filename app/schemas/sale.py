from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    item_id: int
    quantity: int
    total_price: float
    client_id: int

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    class Config:
        from_attributes = True