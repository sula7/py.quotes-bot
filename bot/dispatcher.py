import logging

import aiogram
from aiogram import types

from . import quote


class Dispatcher(aiogram.Dispatcher):
    def __init__(self, dispatcher):
        if dispatcher is None:
            logging.fatal("failed to init dispatcher (none parent class dispatcher)")

        self.dispatcher = dispatcher

        try:
            self.handle_start_command()
        except BaseException:
            logging.error("failed to handle start command")

        try:
            self.handle_quote_command()
        except BaseException:
            logging.error("failed to handle quote command")

        try:
            self.handle_message()
        except:
            logging.error("failed to handle plain text message")

    def handle_message(self):
        @self.dispatcher.message_handler()
        async def echo(message: types.Message):
            await message.answer(message.text)

    def handle_start_command(self):
        @self.dispatcher.message_handler(commands=['start'])
        async def send_welcome(message: types.Message):
            await message.reply("Hi, dude and welcome\nWanna get quote? Type /quote and get first one")

    def handle_quote_command(self):
        @self.dispatcher.message_handler(commands=['quote'])
        async def send_welcome(message: types.Message):
            try:
                q = quote.get_random_quote(message.from_user.language_code)
                await message.reply(q['text'] + '\nAuthor: ' + q['author'])
            except BaseException:
                await message.reply('Something went wrong...')
