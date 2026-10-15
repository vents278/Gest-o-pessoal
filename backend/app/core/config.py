from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Rita & Jean Finance"
    DEBUG: bool = True
    SECRET_KEY: str = "change-me-in-env"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite:///./rita_jean.db"

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
