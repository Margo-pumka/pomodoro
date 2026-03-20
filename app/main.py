from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import routers
from app.consumer import make_amqp_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await make_amqp_consumer()
    yield

app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)
