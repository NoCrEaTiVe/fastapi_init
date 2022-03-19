from loguru import logger
from fastapi import FastAPI
from app.db.database import engine, Base


async def connect_to_db() -> None:
    logger.info("Connecting to Postgres")
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")
    logger.info("Connection closed")
