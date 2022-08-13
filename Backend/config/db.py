from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey , Table
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

tasks = []

engine=create_engine("mysql+pymysql://usuario:1234@localhost:3306/tododb")

conn = engine.connect()

meta=MetaData()

users= Table("user", meta, 
    Column("id",Integer, primary_key=True),
    Column("name",String(255)),
    Column("firstname",String(255)),    
    Column("lastname",String(255)),
    Column("email",String(255)),
    Column("password",String(255)),
    Column("deleted",Boolean,default=False)
    )

tasks=Table("task",meta,
    Column("id", Integer, primary_key=True),
    Column("id_user", Integer, ForeignKey("user.id")),
    Column("tittle", String(255)),
    Column("summary", String(255)),
    Column("date_ini", DateTime),
    Column("date_end", DateTime),
    Column("completed", Boolean,default=False),
    Column("deleted", Boolean,default=False)
    )
meta.create_all(engine)