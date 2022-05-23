from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

barcha_tezliklar = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Tezlik50 50-60'),
            KeyboardButton(text='Tezlik50 70-80'),
            KeyboardButton(text='Tezlik50 80+'),
        ],
        [

            KeyboardButton(text='Tezlik70 70-80'),
            KeyboardButton(text='Tezlik70 80-90'),
            KeyboardButton(text='Tezlik70 90+'),
            KeyboardButton(text='Tezlik70 70-80'),
            KeyboardButton(text='Tezlik70 80-90'),
            KeyboardButton(text='Tezlik70 90+'),
        ]
    ],
    resize_keyboard=True
)