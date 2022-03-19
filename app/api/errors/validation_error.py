from typing import Union

from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def validation_exception_handler(_: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    errors_dict = {"detail": [exc.errors()]}
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=errors_dict,
    )