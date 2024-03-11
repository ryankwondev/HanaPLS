from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str
    MONGODB_HOST: str
    MONGODB_PORT: int


settings = Settings()

if __name__ == "__main__":
    print(settings.dict())
