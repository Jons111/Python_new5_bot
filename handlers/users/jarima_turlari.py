from aiogram import types
from keyboards.default.tezlik_buttons import barcha_tezliklar
from loader import dp


# Echo bot
@dp.message_handler(text='Tezliklar')
async def bot_echo(message: types.Message):
    await message.answer(text="Tezlik turlaridan birini tanlang",reply_markup=barcha_tezliklar)
