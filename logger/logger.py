import logging


def setup(log_level:str):
    logging.basicConfig(
        level=log_level.upper(),
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
