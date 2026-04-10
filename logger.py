# app/core/logger.py

import logging
import sys
import uuid
from contextvars import ContextVar

# Context variable for request ID
request_id_ctx_var: ContextVar[str] = ContextVar("request_id", default=None)


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_ctx_var.get() or "N/A"
        return True


def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [request_id=%(request_id)s] %(message)s"
    )

    handler.setFormatter(formatter)
    handler.addFilter(RequestIdFilter())

    logger.addHandler(handler)

    return logger


logger = setup_logger()


# Middleware helper
def generate_request_id():
    return str(uuid.uuid4())