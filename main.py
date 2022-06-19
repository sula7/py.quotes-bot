import aiogram
from aiogram import Bot, executor

import logger.logger as logger
from bot.dispatcher import Dispatcher
from config.config import Config

app_config = Config()
app_logger = logger.setup(log_level=app_config.get_logger_level())

bot = Bot(token=app_config.get_telegram_bot_token())
dp = Dispatcher(aiogram.Dispatcher(bot))

if __name__ == '__main__':
    executor.start_polling(dp.dispatcher)
