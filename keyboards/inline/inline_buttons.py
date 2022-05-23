from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

barcha_inline_tugmalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='UZB',callback_data='til1'),
            InlineKeyboardButton(text="RUS",callback_data='til2'),
            InlineKeyboardButton(text='Hamkorlarimiz',url='https://t.me/UstozShogird'),
            InlineKeyboardButton(text='Ulashish',switch_inline_query="Zo'r bot ekan ishlatib ko'ringlar ")
        ]
    ]
)