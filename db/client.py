from pymongo import MongoClient


def get_mongo_client(mongo_host: str, mongo_user: str, mongo_password: str) -> MongoClient:
    if _is_ip_address(mongo_host):
        uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}"
    else:
        uri = f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_host}"

    return MongoClient(
        uri,
        socketTimeoutMS=120000,
        serverSelectionTimeoutMS=30000,
        maxPoolSize=5,
    )


def _is_ip_address(host: str) -> bool:
    parts = host.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            number = int(part)
            if number < 0 or number > 255:
                return False
        except ValueError:
            return False
    return True
