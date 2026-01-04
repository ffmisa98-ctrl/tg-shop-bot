import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8568437699:AAG6P6sJKmXiFddbeznOFcv0uekYLJn_K2A"
ADMIN_ID = 7300909934

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🛒 Магазин\n\n"
        "💳 Оплата: перевод на Сбер\n"
        "📞 Номер: 79608581114\n\n"
        "После оплаты напиши админу"
    )

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Напиши /start")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
