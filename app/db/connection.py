from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from loguru import logger
from fastapi import FastAPI
from app.core.settings.app import AppSettings


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    logger.info("Connecting to PostgreSQL")
    app.state.engine = create_async_engine(
        settings.database_url,
        pool_size=0,
        echo=False
    )
    app.state.async_session = sessionmaker(
        bind=app.state.engine, autoflush=False, future=True, class_=AsyncSession
    )
    app.state.Base = declarative_base()


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")
    logger.info("Connection closed")