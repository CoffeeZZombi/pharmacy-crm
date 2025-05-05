from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud
from app.schemas.sale import Sale, SaleCreate

router = APIRouter(prefix="/sales", tags=["Sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Sale)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    result = crud.sale.create_sale(db, sale)
    if not result:
        raise HTTPException(status_code=400, detail="Insufficient quantity or item not found")
    return result

@router.get("/", response_model=list[Sale])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.sale.get_sales(db, skip=skip, limit=limit)