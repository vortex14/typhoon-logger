from logger import get_logger

LOG = get_logger(name="my_app", component="component")
LOG.info("first log", details={"key1": 1, "key2": "string"})