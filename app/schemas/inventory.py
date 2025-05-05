from pydantic import BaseModel
from datetime import datetime

class InventoryBase(BaseModel):
    item_id: int
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    class Config:
        from_attributes = True