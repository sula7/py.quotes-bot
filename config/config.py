import logging
import os


class Config():
    def __init__(self):
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        if bot_token is None:
            logging.fatal("failed to get TELEGRAM_BOT_TOKEN env var")
        self.telegram_bot_token = bot_token

        logger_level = os.getenv("LOGGER_LEVEL")
        if logger_level is None:
            logging.fatal("failed to get LOGGER_LEVEL env var")
        self.logger_level = logger_level

    def get_telegram_bot_token(self):
        return self.telegram_bot_token

    def get_logger_level(self):
        return self.logger_level
