from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Murojat
from loader import dp, bot
from keyboards.default.tasdiqlash import tasdiqlash_tugmalari
from keyboards.inline.inline_buttons import barcha_inline_tugmalar
# Echo bot
@dp.message_handler(text='Murojat qilish')
async def bot_echo(message: types.Message):

    await message.answer(text="Ismni kiriting ")
    await Murojat.ism_qabul_qilish_holat.set()


@dp.message_handler(state=Murojat.ism_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    www = message.text
    await state.update_data({'name':www})
    await message.answer(text="Familayani kiriting ")

    await Murojat.fam_qabul_qilish_holat.set()


@dp.message_handler(state=Murojat.fam_qabul_qilish_holat)
async def bot_echo(message: types.Message, state: FSMContext):
    fam = message.text
    await state.update_data({'familya': fam})
    await message.answer(text="Yoshni kiriting ")

    await Murojat.yosh_qabul_qilish_holat.set()

@dp.message_handler(state=Murojat.yosh_qabul_qilish_holat)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({'yosh': yosh})
    await message.answer(text="Telni  kiriting ")

    await Murojat.tel_qabul_qilish_holat.set()

@dp.message_handler(state=Murojat.tel_qabul_qilish_holat)
async def bot_echo(message: types.Message, state: FSMContext):
    tel = message.text
    if tel.isdigit():
        await state.update_data({'tel': tel})
        await message.answer(text="Murojatni  kiriting ")
        await Murojat.murojat_qabul_qilish_holat.set()
    else:
        await message.answer(text="Bunday tel mavjud emas qayta kiriting ")
        await Murojat.tel_qabul_qilish_holat.set()

@dp.message_handler(state=Murojat.murojat_qabul_qilish_holat)
async def bot_echo(message: types.Message, state: FSMContext):
    murojat = message.text
    await state.update_data({'murojat': murojat})
    foydalanuvchi_malumotlari =await state.get_data()
    user_name = foydalanuvchi_malumotlari.get('name')
    familya = foydalanuvchi_malumotlari.get('familya')
    yosh = foydalanuvchi_malumotlari.get('yosh')
    tel = foydalanuvchi_malumotlari.get('tel')
    ariza = foydalanuvchi_malumotlari.get('murojat')

    matn = f"👨‍⚕️  Ism {user_name}\n" \
           f"🧔‍♂️  Familya {familya}\n" \
           f"👨‍🦰    Yosh {yosh}\n" \
           f"📞      Tel : {tel} \n" \
           f"📌      Murojat {ariza}"
    await message.answer(text=matn,reply_markup=tasdiqlash_tugmalari)
    await Murojat.tasdiqlash_holat.set()


@dp.message_handler(text='Tasdiqlash',state=Murojat.tasdiqlash_holat)
async def bot_echo(message: types.Message, state: FSMContext):
    nick_name = message.from_user.username
    foydalanuvchi_malumotlari = await state.get_data()
    user_name = foydalanuvchi_malumotlari.get('name')
    familya = foydalanuvchi_malumotlari.get('familya')
    yosh = foydalanuvchi_malumotlari.get('yosh')
    tel = foydalanuvchi_malumotlari.get('tel')
    ariza = foydalanuvchi_malumotlari.get('murojat')

    matn = f"👨‍⚕️  Ism {user_name}\n" \
           f"🧔‍♂️  Familya {familya}\n" \
           f"👨‍🦰    Yosh {yosh}\n" \
           f"📞      Tel : {tel} \n" \
           f"📌      Murojat {ariza}\n" \
           f"Ushbu foydalanuvchi habar yubordi {nick_name}"
    await bot.send_message(chat_id='1892438581',text=matn)
    await message.answer(text='Botga hush kelibsiz',reply_markup=barcha_inline_tugmalar)
    await message.answer(text='www',reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(text='Bekor qilish',state=Murojat.tasdiqlash_holat)
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bekor qilindi ',reply_markup=barcha_inline_tugmalar)
    await message.answer(text='www', reply_markup=ReplyKeyboardRemove())
    await state.finish()