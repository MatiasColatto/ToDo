from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from uuid  import uuid4
from config.db import engine ,  conn , tasks


# Local imports
from schemas import Task
from config.db import tasks


task = APIRouter()

#Method for Task
@task.get('/{id_user}')
def get_all_task(id_user: str):
    return conn.execute(tasks.select().where(tasks.c.id_user == id_user)).fetchall()

@task.get('/{id_user}/{id}')
def get_task(id_user: str, id: str):
    return conn.execute(tasks.select().where(tasks.c.id == id and tasks.c.id_user == id_user)).first()

@task.post('/{id_user}')
def create_task(id_user: str, task: Task):
    task.id_user=id_user
    new_task={"id_user":task.id_user,"tittle":task.tittle,"summary":task.summary,"date_end":task.date_end,"date_ini":task.date_ini,"completed":task.completed,"deleted":task.deleted}
    res=conn.execute(tasks.insert().values(new_task))
    return conn.execute(tasks.select().where(tasks.c.id == res.lastrowid)).first()


@task.put('/{id_user}/{id}')
def update_task(id_user: str, id: str, task: Task):
    conn.execute(tasks.update().values(tittle=task.tittle, summary=task.summary, date_end=task.date_end).where(tasks.c.id == id and tasks.c.id_user == id_user))
    return conn.execute(tasks.select().where(tasks.c.id == id and tasks.c.id_user == id_user)).first()


@task.delete('/{id_user}/{id}')
def delete_task(id_user: str, id: str):
    conn.execute(tasks.delete().where(tasks.c.id == id and tasks.c.id_user == id_user))
    return conn.execute(tasks.select().where(tasks.c.id == id and tasks.c.id_user == id_user)).first()