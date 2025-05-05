# app/crud/client.py

from sqlalchemy.orm import Session
from app.models.client import Client as ClientModel
from app.schemas.client import ClientCreate, Client

def create_client(db: Session, client: ClientCreate):
    db_client = ClientModel(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ClientModel).offset(skip).limit(limit).all()
