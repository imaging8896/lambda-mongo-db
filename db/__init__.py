import os

from pymongo import MongoClient

from .logger import logger


MONGO_DB_HOST = os.environ["MONGO_DB_HOST"]
MONGO_DB_USER = os.environ["MONGO_DB_USER"]
MONGO_DB_PASSWORD = os.environ["MONGO_DB_PASSWORD"]
MONGO_DB_CLIENT = MongoClient(
    f"mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}", 
    socketTimeoutMS=120000, 
    serverSelectionTimeoutMS=30000, 
    maxPoolSize=5,
)


def list_collections(db: str):
    logger.warning(f"list_collections({db=})")
    return MONGO_DB_CLIENT[db].list_collection_names()
