from pydantic import BaseModel
from datetime import datetime
from typing import Text, Optional
from uuid import uuid4

class Task(BaseModel):
    id: Optional[int]
    id_user: Optional[int]
    tittle: str
    summary: Text
    date_ini: datetime = datetime.now()
    date_end: datetime
    completed: bool = False
    deleted: bool = False

class User(BaseModel):
    id: Optional[int]
    name: str
    firstname: str
    lastname: str
    email: str
    password: str
    deleted: bool = False

