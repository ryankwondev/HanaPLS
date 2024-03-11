from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str
    MONGODB_HOST: str
    MONGODB_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()

if __name__ == "__main__":
    print(settings.dict())
