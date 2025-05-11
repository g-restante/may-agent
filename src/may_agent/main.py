from embedding import views as embedding_views
from fastapi.middleware.cors import CORSMiddleware
from ask import views as ask_views
from fastapi import FastAPI

# we create the Web API framework
app = FastAPI(
    title="Ask My Docs",
    description="Welcome to Ask My Docs's API documentation! Here you will able to discover all of the ways you can interact with the Ask My Docs API.",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)

# Configura gli allowed origins (localhost:3000 nel tuo caso)
origins = [
    "http://localhost:3000",
    # aggiungi anche altri se necessario, es: "https://tuodominio.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # oppure ["*"] per permettere tutti (non consigliato in prod)
    allow_credentials=True,
    allow_methods=["*"],             # oppure ["GET", "POST", ...]
    allow_headers=["*"],
)

app.include_router(embedding_views.router, prefix="/api/v1/embedding", tags=["embedding"])
app.include_router(ask_views.router, prefix="/api/v1/ask", tags=["ask"])
