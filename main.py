echo "
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('📥 Получить токены'))
    await message.answer('Привет! Добро пожаловать в Divine Purpose Airdrop 🌟', reply_markup=markup)

@dp.message_handler(lambda message: message.text == '📥 Получить токены')
async def airdrop(message: types.Message):
    await message.answer('🪂 Чтобы получить токены:\n\n1. Подпишитесь на канал: https://t.me/Divine_Purpose_Token\n2. Отправьте свой адрес MetaMask ниже:')

@dp.message_handler()
async def wallet(message: types.Message):
    wallet = message.text
    await message.answer(f'✅ Ваш адрес получен: {wallet}\nВы получите 50 DVP в течение 24 часов!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
" > main.py
