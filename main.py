from src.DataScienceWorkflow import logger
from src.DataScienceWorkflow.utils.common import (
    read_yaml,
    create_directories,
    save_json,
    load_json)

logger.info("Welcome to custom logging data science")

logger.info(read_yaml("params.yaml"))

create_directories(["abc"])
save_json("abc/mike.json", {"mike": "test"})
print(load_json("abc/mike.json"))