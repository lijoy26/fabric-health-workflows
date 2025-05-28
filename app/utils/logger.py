import logging

BASE_FORMAT = "%(asctime)-15s %(name)s - %(levelname)s %(message)s"

def init_logger():
    root_logger = logging.getLogger()
    if not root_logger.hasHandlers():
        logging.basicConfig(format=BASE_FORMAT, level=logging.DEBUG)

def get_logger(name):
    init_logger()
    return logging.getLogger(name)
