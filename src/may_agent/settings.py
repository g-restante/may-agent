from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path=dotenv_path)

class Settings(BaseSettings):
    log_level: str = os.getenv("LOG_LEVEL")
    log_format: str = os.getenv("LOG_FORMAT")
    log_datefmt: str = os.getenv("LOG_DATEFMT")
    allowed_origins: str = os.getenv("ALLOWED_ORIGINS")
    embedding_model: str = os.getenv("EMBEDDING_MODEL")
    llm_model: str = os.getenv("LLM_MODEL")
    db_location: str = os.getenv("DB_LOCATION")
    env: str = os.getenv("ENV")
    debug: bool = os.getenv("DEBUG").lower() == "true"

settings = Settings()