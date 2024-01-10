from contextlib import asynccontextmanager

from fastapi import FastAPI

from settings import Settings
from database import create_db_and_tables
from views import router
from utils.logger import logger_config

logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    logger.info("startup: triggered")

    yield

    logger.info("shutdown: triggered")


def create_app(settings: Settings):
    app = FastAPI(
        title="URL Shorter",
        version=settings.VERSION,
        docs_url="/",
        lifespan=lifespan,
    )

    app.include_router(router)

    return app
