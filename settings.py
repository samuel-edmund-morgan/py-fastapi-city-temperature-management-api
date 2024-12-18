from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI City Temperature Management API"

    DATABASE_URL: str | None = "sqlite:///./city-management.db"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()