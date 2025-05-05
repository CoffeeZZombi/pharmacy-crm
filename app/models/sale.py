from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from app.database import Base
from datetime import datetime

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    client_id = Column(Integer)