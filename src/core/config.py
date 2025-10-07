from pydantic_settings import BaseSettings , SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI App"
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()