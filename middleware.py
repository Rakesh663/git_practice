# app/core/middleware.py

import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.logger import logger, request_id_ctx_var, generate_request_id


class RequestContextMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # 🔹 Generate request ID
        request_id = generate_request_id()
        request_id_ctx_var.set(request_id)

        start_time = time.time()

        # 🔹 Log request start
        logger.info(
            f"Request started | method={request.method} path={request.url.path}"
        )

        try:
            response: Response = await call_next(request)

        except Exception as e:
            logger.exception(
                f"Unhandled error | method={request.method} path={request.url.path}"
            )
            raise e

        process_time = time.time() - start_time

        # 🔹 Log request end
        logger.info(
            f"Request completed | status={response.status_code} "
            f"time={process_time:.4f}s"
        )

        # 🔹 Attach request_id to response
        response.headers["X-Request-ID"] = request_id

        return response