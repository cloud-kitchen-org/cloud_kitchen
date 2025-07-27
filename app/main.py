from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from contextlib import asynccontextmanager

from app.api.v1 import api_router
from app.core.logger import Logger

logger = Logger.get_logger(__name__)


# Lifespan: startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up FastAPI application...")
    # Place startup tasks here (e.g., DB health checks, background tasks)
    yield
    logger.info("Shutting down FastAPI application...")
    # Place cleanup tasks here (e.g., closing connections)
    logger.info("Shutdown complete. Resources cleaned. Bye")


# Initialize app

app = FastAPI(title="Cloud Kitchen Platform", version="1.0.0", lifespan=lifespan)


# Add Bearer token security scheme to OpenAPI docs
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="Cloud Kitchen Platform API",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# Allow CORS for frontend during dev
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API router
app.include_router(api_router, prefix="/api/v1")
