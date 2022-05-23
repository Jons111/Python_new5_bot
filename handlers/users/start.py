import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.jarimalar_buttons import barcha_jarimalar
from keyboards.inline.inline_buttons import barcha_inline_tugmalar
from loader import dp,baza,bot
from filters import Shaxsiy


@dp.message_handler(Shaxsiy(),CommandStart(),)
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    user_name = message.from_user.username
    t_id = message.from_user.id
    try:
        baza.odam_qoshish(ism = ism,tg_id=t_id,fam=fam,username=user_name)
    except Exception:
        pass
    await message.answer(f"Assalomu alaykum jarima botga hush kelibsiz, {message.from_user.full_name}!",reply_markup=barcha_inline_tugmalar)

@dp.message_handler(Shaxsiy(),commands='all_users',chat_id ='1892438581')
async def bot_start(message: types.Message):
    son = baza.userlar_soni()
    vaqt = datetime.datetime.now()
    await message.answer(text= f" botda {son} ta foydalanuvchi mavjud {vaqt}")


@dp.message_handler(Shaxsiy(),commands='post',chat_id ='1892438581')
async def bot_start(message: types.Message):

    """



    """
    userlar = baza.select_barcha_userlar()
    for user in userlar:
        await bot.send_message(chat_id=user[3],text="Reklama: salom ")
