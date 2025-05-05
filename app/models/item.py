from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    manufacturer = Column(String(255))
    purchase_price = Column(Float)
    sale_price = Column(Float)
    stock_quantity = Column(Integer)
    category = Column(String(255))