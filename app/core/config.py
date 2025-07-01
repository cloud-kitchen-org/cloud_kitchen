from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "FoodOrderApp"
    LOGGING_LEVEL: str = "info"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    ENV: str = "development"  # development | staging | production

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENV', 'development')}",  # dynamically pick env file
        env_file_encoding="utf-8",
    )


settings = Settings()
