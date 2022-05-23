from aiogram import types
from aiogram.types import ContentType, InputFile

from loader import dp,bot


# Echo bot
@dp.message_handler(commands='rasm')
async def bot_echo(message: types.Message):
    await message.answer(text='dakument yuboring ')

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[1].download()
    rasm_id = message.photo[1].file_id
    await message.answer(text=f"rasm qabul qilindi shu Idda {rasm_id}")

@dp.message_handler(content_types=ContentType.STICKER)
async def bot_echo(message: types.Message):
    await message.sticker.download()
    await message.answer(text="Stiker qabul qilindi")

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text="Video qabul qilindi")

@dp.message_handler(text='Remen')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzil = 'https://t.me/UstozShogird/17932'
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,
                         caption="Taom nomi :Osh"
                                 "Narx       :20000 ")

@dp.message_handler(text='Svetafor')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = 'https://t.me/UzPythonMeetup/164'
    await bot.send_video(chat_id=user_id,video=video_manzil,
                         caption="Taom nomi :Osh"
                                 "Narx       :20000 ")