from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from starlette.responses import Response

from config import Settings, settings
from utils.logger import setup_logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, settings: Settings):
        super().__init__(app)
        self.settings = settings

    async def dispatch(self, request: Request, call_next):
        req_body = await request.body()
        response = await call_next(request)

        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk
        
        path = "%s/$%sapi_io_%s.log" % (
            self.settings.LOG_PATH,
            datetime.now().strftime("%Y%m%d"),
            request.url.path.strip("/").replace("/", "_")
        )
        log = f"""
[Request] {request.method} {request.url.path}
Headers: {dict(request.headers)}
Body: {req_body.decode() if req_body else None}
[Response] Status: {response.status_code}
Headers: {dict(response.headers)}
Body: {response_body.decode() if response_body else None}

"""
        
        with open(path, "a") as f:
            f.write(log)

        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers)
        )


def create_app() -> FastAPI:
    setup_logger()
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggerMiddleware, settings=settings)

    return app

app = create_app()