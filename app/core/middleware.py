"""
Session Middleware - initializes request.state.session for each request.
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from typing import Callable


class SessionMiddleware(BaseHTTPMiddleware):
    """Initializes request.state.session dict for each request."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request.state.session = {}
        response = await call_next(request)
        return response
