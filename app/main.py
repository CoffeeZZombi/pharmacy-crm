from fastapi import FastAPI
from app.routers import clients, items, sales, inventory

app = FastAPI(title="Pharmacy CRM")

app.include_router(clients.router)
app.include_router(items.router)
app.include_router(sales.router)
app.include_router(inventory.router)