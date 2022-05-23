from typing import Union
from aiogram import Bot
from aiogram.dispatcher.filters import BoundFilter

async def checking(user_id,kanal_link:Union[str,int]):
    bot = Bot.get_current()
    azo = await bot.get_chat_member(user_id=user_id, chat_id=kanal_link)
    return azo.is_chat_member()