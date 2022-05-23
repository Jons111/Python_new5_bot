from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default.jarimalar_buttons import barcha_jarimalar
from loader import dp


# Echo bot
@dp.callback_query_handler(text = 'til1')
async def bot_echo(matn: CallbackQuery):
    await matn.message.answer(text='Quyidagi jarimalardan birini tanlang',reply_markup=barcha_jarimalar)
