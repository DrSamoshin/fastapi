from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask, TaskId
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("")
async def add_tasks(task: Annotated[STaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return task_id


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
