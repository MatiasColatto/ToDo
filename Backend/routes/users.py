from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from uuid  import uuid4
from cryptography.fernet import Fernet
from schemas import User
from config.db import engine ,  conn , users

key = Fernet.generate_key()

f=Fernet(key)

user = APIRouter()

#Method for Users
@user.get("/users",response_model=List[User])
def get_all_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{id}")
def get_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()
    

@user.post("/")
def create_user(user: User):
    new_user= {"name": user.name, "firstname":user.firstname, "lastname":user.lastname, "email":user.email, "deleted":user.deleted}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    res=conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == res.lastrowid)).first()

@user.put("/users/{id}")
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name, lastname=user.lastname, firstname=user.firstname, email=user.email, password=user.password).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete('/{id}')
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()