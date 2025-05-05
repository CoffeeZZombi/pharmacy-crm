from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database import Base
from datetime import datetime

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    stock_quantity = Column(Integer)
    quantity = Column(Integer, nullable=False)