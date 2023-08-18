import telebot
from telebot import types

#bot = telebot.TeleBot('6001758792:AAG7nWtD3dszvLNxHa9NPZFw-bZ3-CFia4w')
bot = telebot.TeleBot('6009673279:AAFcXWpst4TEArigxxa9NHSMsNJaqIOLTt0') # Саша

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, text='Добро пожаловать в бот нашего магазина YoungTEA. По команде /info вы можете \
    подробнее узнать о нашем бренде. Команда /catalog — категории одежды, которая на данный момент есть в наличии.')


@bot.message_handler(commands=['info'])
def information(msg):
    bot.send_message(msg.chat.id, text='Бренд YoungTEA основан в 2017 году в городе Санкт-Петербург.\n Наша миссия — \
    показать, что гардероб молодежи может состоять не только из худи и кроссовок.\n Все модели бренда передают эстетику\
     тихого осеннего вечера с чашкой чая и книгой в руках.')


@bot.message_handler(commands=['catalog'])
def categories(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Обувь')
    btn2 = types.KeyboardButton(text='Верх')
    btn3 = types.KeyboardButton(text='Низ')
    btn4 = types.KeyboardButton(text='Верхняя одежда')
    btn5 = types.KeyboardButton(text='Костюмы и платья')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(msg.chat.id, text='Выберите категорию', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def positions(msg):
    if msg.text == "Обувь":
        img1 = open('ботинки муж.jpg', 'rb')
        img2 = open('лоферы жен.jpg', 'rb')
        img3 = open('туфли жен.jpg', 'rb')
        bot.send_photo(msg.chat.id, img1, caption="Ботинки мужские.\nЦена: 3500.\nарт_001")
        bot.send_photo(msg.chat.id, img2, caption="Лоферы. \n Цена: 2100.\nарт_007")
        bot.send_photo(msg.chat.id, img3, caption="Туфли женские.\nЦена: 2600.\nарт_013")
    if msg.text == "Верх":
        img1 = open('жилет.jpg', 'rb')
        img2 = open('рубашка.jpg', 'rb')
        img3 = open('свитер муж.jpg', 'rb')
        bot.send_photo(msg.chat.id, img1, caption="Жилет мужской.\nЦена: 1800.\nарт_003")
        bot.send_photo(msg.chat.id, img2, caption="Рубашка.\nЦена: 1500.\nарт_011")
        bot.send_photo(msg.chat.id, img3, caption="Свитер.\nЦена: 2400.\nарт_012")
    if msg.text == "Низ":
        img1 = open('брюки муж.jpg', 'rb')
        img2 = open('юбка.jpg', 'rb')
        img3 = open('шорты.jpg', 'rb')
        bot.send_photo(msg.chat.id, img1, caption="Брюки мужские.\nЦена: 2400.\nарт_002")
        bot.send_photo(msg.chat.id, img2, caption="Юбка.\nЦена: 1800.\nарт_015")
        bot.send_photo(msg.chat.id, img3, caption="Шорты утеплённые.\nЦена: 1600.\nарт_014")
    if msg.text == "Верхняя одежда":
        img1 = open('пальто.jpg', 'rb')
        img2 = open('пальто муж.jpg', 'rb')
        img3 = open('кардиган.jpg', 'rb')
        bot.send_photo(msg.chat.id, img1, caption="Пальто женское.\nЦена: 6300.\nарт_009")
        bot.send_photo(msg.chat.id, img2, caption="Пальто мужское.\nЦена: 4900.\nарт_008")
        bot.send_photo(msg.chat.id, img3, caption="Кардиган.\nЦена: 2300.\nарт_004")
    if msg.text == "Костюмы и платья":
        img1 = open('костюм.jpg', 'rb')
        img2 = open('костюм муж.jpg', 'rb')
        img3 = open('платье.jpg', 'rb')
        bot.send_photo(msg.chat.id, img1, caption="Костюм женский.\nЦена: 6000.\nарт_013")
        bot.send_photo(msg.chat.id, img2, caption="Костюм мужской.\nЦена: 5800.\nарт_013")
        bot.send_photo(msg.chat.id, img3, caption="Платье.\nЦена: 1900.\nарт_013")


bot.polling(non_stop=True)
