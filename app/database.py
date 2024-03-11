from pymongo import MongoClient

from config import settings

client = MongoClient(
    host=settings.MONGODB_HOST,
    port=settings.MONGODB_PORT,
    username=settings.MONGODB_USER,
    password=settings.MONGODB_PASSWORD,
)

mongo = client[settings.MONGODB_DATABASE]

if __name__ == "__main__":
    print(client.server_info())
