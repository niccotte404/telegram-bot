from aiogram import Bot
from aiogram.utils.executor import executor
from aiogram.dispatcher import Dispatcher
import config

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await message.reply(config.greeting)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)