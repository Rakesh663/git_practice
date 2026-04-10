# app/core/redis.py

import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


def get_redis_client():
    return redis.Redis.from_url(
        REDIS_URL,
        decode_responses=True
    )


# 👇 CHANGE THIS LINE IN MAIN
redis_client = get_redis_client()
print("Redis initialized from MAIN")