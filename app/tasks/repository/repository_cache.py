from redis import asyncio as Redis

from app.tasks.schema import TaskSchema


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def get_tasks(self) -> list[TaskSchema]:
        async with self.redis as redis:
            tasks_json = await redis.lrange("tasks", 0, -1)
            return [TaskSchema.model_validate_json(task_json) for task_json in tasks_json]

    async def set_task(self, tasks: list[TaskSchema]):
        tasks_json = [task.model_dump_json() for task in tasks]
        async with self.redis as redis:
            await redis.lpush("tasks", *tasks_json)
