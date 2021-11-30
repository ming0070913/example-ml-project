#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import traceback

from fastapi.logger import logger
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from config import CONFIG

def get_error_response(request, exc) -> dict:
    """
    Generic error handling function
    """

    error_response = {
        "error": True,
        "message": str(exc)
    }

    # Return traceback info if debug mode is on
    if CONFIG['DEBUG']:
        error_response["traceback"] = "".join(
            traceback.format_exception(
                etype=type(exc), value=exc, tb=exc.__traceback__
            )
        )

    return error_response

# @router.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handling error in validating requests
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=get_error_response(request, exc)
    )


# @router.exception_handler(Exception)
async def python_exception_handler(request: Request, exc: Exception):
    """
    Handling any internal error
    """

    # Log requester infomation
    logger.error('Request info:\n' + json.dumps({
        "host": request.client.host,
        "method": request.method,
        "url": str(request.url),
        "headers": str(request.headers),
        "path_params": str(request.path_params),
        "query_params": str(request.query_params),
        "cookies": str(request.cookies)
    }, indent=4))

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=get_error_response(request, exc)
    )
