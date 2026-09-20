import os
import logging

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d (%(funcName)s) — %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()
