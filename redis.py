# app/core/redis.py

import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


def get_redis_client():
    return redis.Redis.from_url(
        REDIS_URL,
        decode_responses=True  # returns strings instead of bytes
    )


# Singleton client (optional)
redis_client = get_redis_client()