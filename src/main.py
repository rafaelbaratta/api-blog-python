from contextlib import asynccontextmanager

from fastapi import FastAPI

import src.models
from src.controllers import user_controller
from src.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="API de Blog", lifespan=lifespan)

app.include_router(user_controller.router)
