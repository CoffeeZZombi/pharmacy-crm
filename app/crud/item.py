from sqlalchemy.orm import Session
from app.models.item import Item as ItemModel
from app.schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate):
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemModel).offset(skip).limit(limit).all()
