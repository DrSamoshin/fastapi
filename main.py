from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('DB is deleted')
    await create_tables()
    print('DB is created')
    yield
    print('app is off')


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_tasks(task: Annotated[STaskAdd, Depends()]):
    tasks.append(task)
    return {"ok": True}


@app.get("/tasks")
def get_tasks():
    task = STask(name="First")
    return {"data": task}
