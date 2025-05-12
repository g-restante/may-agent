from embedding import views as embedding_views
from ask import views as ask_views
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import settings
import logging
import os

logging.basicConfig(
    level = settings.log_level.upper(),
    format= settings.log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Ask My Docs",
    description=(
        "Welcome to Ask My Docs's API documentation! "
        "Here you will be able to discover all of the ways you can interact with the Ask My Docs API."
    ),
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
logger.info(f"Allowed origins: {origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(embedding_views.router, prefix="/api/v1/embedding", tags=["embedding"])
app.include_router(ask_views.router, prefix="/api/v1/ask", tags=["ask"])

logger.info("API 'Ask My Docs' started!")
