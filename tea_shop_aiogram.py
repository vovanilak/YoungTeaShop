import logging      # для получения состояния бота
from aiogram import Bot, Dispatcher, filters, types
import os, dotenv

dotenv.load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()               # диспетчер предназначен для обработки апдейтов ("помощник" бота)

# настройка получения логов (состояние бота)
logging.basicConfig(level=logging.INFO)

# настройка команды start
@dp.message(filters.Command('start'))       # фильтр, который получает только КОМАНДЫ со ЗНАЧЕНИЕМ start
async def cmd_start(message: types.Message):# types.Message указывается экземпляр переменной message для подсвтеки синтаксиса
    await message.answer('Добро пожаловать в бот нашего магазина YoungTEA. По команде /info вы можете \
    подробнее узнать о нашем бренде. Команда /catalog — категории одежды, которая на данный момент есть в наличии.')

# настройка команды info
@dp.message(filters.Command('info'))
async def cmd_help(message: types.Message):
    await message.answer('Бренд YoungTEA основан в 2017 году в городе Санкт-Петербург.\nНаша миссия — показать, что гардероб молодежи может состоять не только из худи и кроссовок.\nВсе модели бренда передают эстетику тихого осеннего вечера с чашкой чая и книгой в руках.')

@dp.message(filters.Command('catalog'))
async def cmd_catalog(message: types.Message):
    # создание кнопок
    btn1 = types.KeyboardButton(text='Обувь')
    btn2 = types.KeyboardButton(text='Верх')
    btn3 = types.KeyboardButton(text='Низ')
    btn4 = types.KeyboardButton(text='Верхняя одежда')
    btn5 = types.KeyboardButton(text='Костюмы и платья')
    # настройка порядка кнопок (сколько списков столько и рядов)
    kb = [
        [btn1, btn2, btn3],
        [btn4, btn5]
    ]
    # создание клавиатуры с кнопками
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True    # делает кнпки компактными
    )
    await message.answer("Выберете категорию", reply_markup=keyboard) # отправка текста с клавиатурой

@dp.message(filters.Text)           # фильтр, который получает все текстовые сообщения
async def text_categor(msg: types.Message):
    if msg.text == "Обувь":
        img1 = types.FSInputFile('ботинки муж.jpg')     # открытие файла
        img2 = types.FSInputFile('лоферы жен.jpg')
        img3 = types.FSInputFile('туфли жен.jpg')

        await msg.answer_photo(img1, caption="Ботинки мужские.\nЦена: 3500.\nарт_001") # отправка фото с текстом
        await msg.answer_photo(img2, caption="Лоферы. \n Цена: 2100.\nарт_007")
        await msg.answer_photo(img3, caption="Туфли женские.\nЦена: 2600.\nарт_013")
    if msg.text == "Верх":
        img1 = types.FSInputFile('жилет.jpg')
        img2 = types.FSInputFile('рубашка.jpg')
        img3 = types.FSInputFile('свитер муж.jpg')

        await msg.answer_photo(img1, caption="Жилет мужской.\nЦена: 1800.\nарт_003")
        await msg.answer_photo(img2, caption="Рубашка.\nЦена: 1500.\nарт_011")
        await msg.answer_photo(img3, caption="Свитер.\nЦена: 2400.\nарт_012")
    if msg.text == "Низ":
        img1 = types.FSInputFile('брюки муж.jpg', 'rb')
        img2 = types.FSInputFile('юбка.jpg')
        img3 = types.FSInputFile('шорты.jpg')

        await msg.answer_photo(img1, caption="Брюки мужские.\nЦена: 2400.\nарт_002")
        await msg.answer_photo(img2, caption="Юбка.\nЦена: 1800.\nарт_015")
        await msg.answer_photo(img3, caption="Шорты утеплённые.\nЦена: 1600.\nарт_014")
    if msg.text == "Верхняя одежда":
        img1 = types.FSInputFile('пальто.jpg', 'rb')
        img2 = types.FSInputFile('пальто муж.jpg')
        img3 = types.FSInputFile('кардиган.jpg')

        await msg.answer_photo(img1, caption="Пальто женское.\nЦена: 6300.\nарт_009")
        await msg.answer_photo(img2, caption="Пальто мужское.\nЦена: 4900.\nарт_008")
        await msg.answer_photo(img3, caption="Кардиган.\nЦена: 2300.\nарт_004")
    if msg.text == "Костюмы и платья":
        img1 = types.FSInputFile('костюм.jpg', 'rb')
        img2 = types.FSInputFile('костюм муж.jpg')
        img3 = types.FSInputFile('платье.jpg')

        await msg.answer_photo(img1, caption="Костюм женский.\nЦена: 6000.\nарт_013")
        await msg.answer_photo(img2, caption="Костюм мужской.\nЦена: 5800.\nарт_013")
        await msg.answer_photo(img3, caption="Платье.\nЦена: 1900.\nарт_013")


if __name__ == "__main__":  # если файл запускается, а не импортируется (если этого не сделать, то при импорте файла он будет запускаться)
    dp.run_polling(bot)     # запуск бота