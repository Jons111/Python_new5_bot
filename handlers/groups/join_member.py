from aiogram import types
from aiogram.types import ContentType

from loader import dp,bot

from filters import Guruh
# Echo bot
@dp.message_handler(Guruh(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text = "Guruhdan start bosdiz ")


@dp.message_handler(Guruh(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
   guruh_id = message.chat.id
   user_name = message.new_chat_members[0].username
   message_id = message.message_id
   # await message.answer(text=f'guruhga hush kelibsiz '
   #                           f'<a href="{user_name}">{user_name}</a>')
   await bot.delete_message(chat_id=guruh_id,message_id=message_id)

@dp.message_handler(Guruh(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
   guruh_id = message.chat.id
   user_name = message.left_chat_member.username
   message_id = message.message_id
   # await message.answer(text=f'guruhga hush kelibsiz '
   #                           f'<a href="{user_name}">{user_name}</a>')
   await bot.delete_message(chat_id=guruh_id,message_id=message_id)