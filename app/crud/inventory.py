from sqlalchemy.orm import Session
from app.models.inventory import Inventory as InventoryModel
from app.models.item import Item as ItemModel
from app.schemas.inventory import InventoryCreate

def add_inventory(db: Session, inv: InventoryCreate):
    db_item = db.query(ItemModel).filter(ItemModel.id == inv.item_id).first()
    if not db_item:
        raise ValueError("Item not found")

    # Обновляем stock_quantity
    db_item.stock_quantity += inv.quantity

    # Сохраняем quantity в inventory
    db_inventory = InventoryModel(item_id=inv.item_id, quantity=inv.quantity)
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def get_inventory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryModel).offset(skip).limit(limit).all()
