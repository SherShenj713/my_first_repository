from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Вставляем токен нашего бота, полученный у @BotFather
BOT_TOKEN = '8062562240:AAHhLjVDzaG0iwH_yiM85wfsNqsmIBS450c'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хендлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет! Меня зовут Эхо-бот! Напиши мне что-нибудь')

# Этот хендлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

# Навешиваем декоратор без фильтров, чтобы ловить большиство апдейтов
@dp.message()
async def process_any_update(message: Message):
    # Выводим апдейт в терминал
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer('Вы что-то прислали!')

# Этот хендлер будет срабатывать на любые ваши сообщения, кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Данный тип апдейтов не поддерживается методом send_copy')

if __name__ == '__main__':
    dp.run_polling(bot)