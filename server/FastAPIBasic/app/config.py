from pydantic import BaseSettings


class Settings(BaseSettings):
    # POSTGRES_HOST: str
    # POSTGRES_PORT: str
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DATABASE: str

    POSTGRES_URL: str
    JWT_SECRET: str

    class Config:
        env_file = ".env"


settings = Settings()
