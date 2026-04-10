# app/main.py

from fastapi import FastAPI, Request
from app.api.router import router
from app.core.logger import request_id_ctx_var, generate_request_id
from app.core.exceptions import (
    app_exception_handler,
    http_exception_handler,
    generic_exception_handler,
    AppException
)
from fastapi import HTTPException

app = FastAPI()

# Register routes
app.include_router(router, prefix="/api")


# 🔹 Middleware for request_id
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = generate_request_id()
    request_id_ctx_var.set(request_id)

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id

    return response


# 🔹 Exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)