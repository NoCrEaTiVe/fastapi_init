from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from fastapi.exceptions import RequestValidationError

from app.core.config import get_app_settings
from app.core.events import create_start_app_handler
from app.api.errors.validation_error import validation_exception_handler

from app.api.routes.auth import router


def get_application() -> FastAPI:

    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    add_pagination(application)
    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.include_router(router)
    application.add_exception_handler(RequestValidationError, validation_exception_handler)
    return application


app = get_application()
