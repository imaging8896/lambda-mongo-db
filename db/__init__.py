import os

from .client import get_mongo_client
from .logger import logger


MONGO_DB_HOST = os.environ["MONGO_DB_HOST"]
MONGO_DB_USER = os.environ["MONGO_DB_USER"]
MONGO_DB_PASSWORD = os.environ["MONGO_DB_PASSWORD"]


MONGO_DB_CLIENT = get_mongo_client(
    mongo_host=MONGO_DB_HOST,
    mongo_user=MONGO_DB_USER,
    mongo_password=MONGO_DB_PASSWORD,
)


def list_collections(db: str):
    logger.warning(f"list_collections({db=})")
    return MONGO_DB_CLIENT[db].list_collection_names()
