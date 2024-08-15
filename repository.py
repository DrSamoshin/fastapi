from sqlalchemy import select
from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:

    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            data_dict = data.model_dump()
            task = TaskOrm(**data_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [STask.model_validate(task) for task in task_models]
            return tasks_schemas
