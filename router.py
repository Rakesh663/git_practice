# app/api/router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.exceptions import ResourceNotFoundError
from app.core.logger import logger

router = APIRouter()


# 🔹 Fake DB model (for demo)
fake_users = {
    1: {"id": 1, "name": "Rocky"},
    2: {"id": 2, "name": "Ravi"},
}


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching user {user_id}")

    user = fake_users.get(user_id)

    if not user:
        logger.warning(f"User {user_id} not found")
        raise ResourceNotFoundError("User")

    return {
        "success": True,
        "data": user
    }


@router.post("/users")
def create_user(name: str, db: Session = Depends(get_db)):
    logger.info(f"Creating user {name}")

    new_id = max(fake_users.keys()) + 1
    fake_users[new_id] = {"id": new_id, "name": name}

    return {
        "success": True,
        "data": fake_users[new_id]
    }