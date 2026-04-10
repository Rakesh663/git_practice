# app/core/exceptions.py

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


# 🔹 Custom Exceptions

class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


class ResourceNotFoundError(AppException):
    def __init__(self, resource: str = "Resource"):
        super().__init__(f"{resource} not found", 404)


class ConflictError(AppException):
    def __init__(self, message: str = "Conflict occurred"):
        super().__init__(message, 409)


# 🔹 Global Exception Handler

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message,
            "path": str(request.url)
        }
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail,
            "path": str(request.url)
        }
    )


async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error",
            "details": str(exc),
            "path": str(request.url)
        }
    )