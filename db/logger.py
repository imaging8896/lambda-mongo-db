import logging
import sys


logger = logging.getLogger("db")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)
