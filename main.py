# app/main.py

from fastapi import FastAPI
from app.api.router import router
from app.core.middleware import RequestContextMiddleware

app = FastAPI()
<<<<<<< HEAD

print("merge conflicts in main")

print("merge confllicts in test3")

# 🔹 Add middleware
||||||| parent of 0a02c0f (Feature3: update main.py)
print("merge confllicts in test3")
# 🔹 Add middleware
=======
print("merge confllicts in test3 branch")
 # Add middleware
>>>>>>> 0a02c0f (Feature3: update main.py)
app.add_middleware(RequestContextMiddleware)

# 🔹 Routes
app.include_router(router, prefix="/api")