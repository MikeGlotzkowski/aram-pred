import logging
from datetime import datetime
import pathlib


def initialize(name):
    logger_name = name
    logger_level = logging.DEBUG
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    date_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    pathlib.Path('./logs/').mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(
        "./logs/{0}_{1}".format(date_time, logger_name))
    ch.setLevel(logger_level)
    fh.setLevel(logger_level)
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

initialize('default')
