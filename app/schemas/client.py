from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    email: str
    phone_number: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
