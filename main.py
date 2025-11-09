import traceback

from db.logger import logger
from db import list_collections


def handler(event=None, context=None):
    try:
        logger.warning(f"Received: {event=} {context=}")
        if not isinstance(event, dict):
            raise ValueError("Must provide event as dict")

        if "action" not in event:
            raise ValueError("Missing action in event")
        
        action_func = {
            "list_collections": list_collections,
        }[event.pop("action")]

        data = action_func(**event)
        return {
            "status": True,
            "result": {
                "data": data,
            },
        }
    except Exception as e:
        return {
            "status": False,
            "result": {
                "exception_type": str(type(e)),
                "exception_message": str(e),
                "traceback" : traceback.format_exc(),
            },
        }        
