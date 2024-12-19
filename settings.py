from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI City Temperature Management API"

    DATABASE_URL: str | None = "sqlite:///./city-management.db"

    OPEN_WEATHER_API_KEY: str = "dd5739f4fbb18df732b3e40b853d1f90"
    OPEN_WEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5/weather?"
    KELVIN_TO_CELSIUS: float = 273.15

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()