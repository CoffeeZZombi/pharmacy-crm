from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud
from app.schemas.inventory import Inventory, InventoryCreate

router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Inventory)
def add_inventory(inv: InventoryCreate, db: Session = Depends(get_db)):
    return crud.inventory.add_inventory(db, inv)

@router.get("/", response_model=list[Inventory])
def read_inventory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.inventory.get_inventory(db, skip=skip, limit=limit)