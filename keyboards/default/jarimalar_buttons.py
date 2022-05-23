from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


barcha_jarimalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tezliklar"),

        ],
        [
            KeyboardButton(text="Remen"),
            KeyboardButton(text="Svetafor"),
            KeyboardButton(text='Strech')
        ],
[
            KeyboardButton(text="Telefon"),
            KeyboardButton(text='Lokatsiya',request_location=True),
            KeyboardButton(text='Kontakt',request_contact=True),

        ],
        [
            KeyboardButton(text='Murojat qilish')
        ]

    ],
    resize_keyboard=True
)
