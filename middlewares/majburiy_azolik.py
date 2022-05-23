from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from data.config import kanallar
from data.tekshirish import checking
from loader import bot,dp
from keyboards.default.jarimalar_buttons import barcha_jarimalar


class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = 'Quyidagi kanalga azo boling\n'

        daslabki_holati = True
        tugmalar = []
        index=0
        for k in kanallar:
            holat = await checking(user_id=user_id,kanal_link=k)
            daslabki_holati *= holat

            kanal = await bot.get_chat(k)
            i = 0
            if not holat:
                link = await kanal.export_invite_link()
                if i % 2 == 0 and i != 0:
                    index += 1

                if i % 2 == 0:
                    tugmalar.append([InlineKeyboardButton(text=f'{kanal.title}',url=f'{link}')])
                else:
                    tugmalar[index].append(InlineKeyboardButton(text=f'{kanal.title}',url=f'{link}'))
                i += 1


        if not daslabki_holati:
            tugmalar.append([InlineKeyboardButton(text=f'Tekshirish', callback_data='check')])
            await bot.send_message(chat_id=user_id, text=matn,
                                   reply_markup=InlineKeyboardMarkup(inline_keyboard=tugmalar))
            raise CancelHandler()


@dp.callback_query_handler(text='check')
async def check(xabar:CallbackQuery):
   user_id= xabar.from_user.id
   await bot.send_message(chat_id=user_id,text="Botdan foydalanishiz mumkin",reply_markup=barcha_jarimalar)


@dp.message_handler(commands='reklama',chat_id = '1892438581')
async def sending(xabar:types.Message):

    for kanal in kanallar:
        await bot.send_message(chat_id=kanal,text="botdan xabar yuborildi ")
