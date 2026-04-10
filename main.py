# app/main.py

from fastapi import FastAPI
from app.api.router import router
from app.core.middleware import RequestContextMiddleware

app = FastAPI()

# 🔹 Add middleware
app.add_middleware(RequestContextMiddleware)

# 🔹 Routes
app.include_router(router, prefix="/api")