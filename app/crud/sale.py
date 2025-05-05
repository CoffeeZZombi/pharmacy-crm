from sqlalchemy.orm import Session
from app.models.sale import Sale as SaleModel
from app.models.item import Item as ItemModel
from app.schemas.sale import SaleCreate

def create_sale(db: Session, sale: SaleCreate):
    db_item = db.query(ItemModel).filter(ItemModel.id == sale.item_id).first()
    if not db_item or db_item.stock_quantity < sale.quantity:
        return None
    db_item.stock_quantity -= sale.quantity
    db_sale = SaleModel(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SaleModel).offset(skip).limit(limit).all()
