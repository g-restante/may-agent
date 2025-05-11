from embedding import views as embedding_views
from ask import views as ask_views
from fastapi import FastAPI

# we create the Web API framework
app = FastAPI(
    title="Ask My Docs",
    description="Welcome to Ask My Docs's API documentation! Here you will able to discover all of the ways you can interact with the Ask My Docs API.",
    root_path="/api/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)

app.include_router(embedding_views.router, prefix="/api/v1/embedding", tags=["embedding"])
app.include_router(ask_views.router, prefix="/api/v1/ask", tags=["ask"])
