import random
import telebot
import webbrowser
from telebot import types


# Считываю свой токен из файла mytoken.txt, в твоем случае это будет не нужно
# Удали 6 и 7 строчки и вместо переменной mytoken в 10 строчке напиши свой токен
# Пример: bot = telebot.TeleBot('62732:RyJidSDIdi...')
PayToken = "1744374395:TEST:b6606f959a8b1054e7d8"
mytoken = "5897951595:AAHmuSh-hsPamlrcORlFILI8D7dQDiinpD0"
idPhoto = 0
# Передаем сюда токен, который получили от FatherBot
bot = telebot.TeleBot(mytoken)
# Варианты ответов пользователю, если тот ввел непонятное боту сообщение
answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # Добавляем кнопки, которые будут появляться после ввода команды /start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button3 = types.KeyboardButton('📄 Справка')
    # Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок
    markup.row(button1)

    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакт моего разработчика: https://t.me/Evirde', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)

# Обработка фото. Если пользователь пришлет фото, то бот отреагирует на него. Можно реализовать свой функционал
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        goodsChapter(message)
    elif message.text == '📄 Справка':
        infoChapter(message)
    elif message.text == '🔹 Товар #1':
        global idPhoto 
        idPhoto = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Эрчим люто лыбиться\n-10 рублей', reply_markup=markup)
    elif message.text == '🔹 Товар #2':

        idPhoto = 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Эрчим яблоко жует\n-10 рублей', reply_markup=markup)
    elif message.text == '🔹 Товар #3':

        idPhoto = 3
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Эрчим показывает язык\n-10 рублей', reply_markup=markup)
    elif message.text == '🔹 Товар #4':

        idPhoto = 4
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Эрчим качек из тим фортресс\n-10 рублей', reply_markup=markup)
    elif message.text == "💳 Купить":
        succes(message)
        PayPhoto(message)
    elif message.text == '💳 Купить' or message.text == '✏️ Написать разработчику':
        # Сюда можете ввести свою ссылку на Телеграмм, тогда пользователя будет перекидывать к вам в личку
        webbrowser.open('https://t.me/Evirde')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    # Если пользователь написал свое сообщение, то бот рандомно генерирует один из возможных вариантов ответа
    # Добавлять и редактировать варианты ответов можно в списке answers
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

def PayPhoto(message):
    bot.send_invoice(message.chat.id, "Покупка фото","Покупка фото Эрчима","invoice", PayToken, "RUB", [types.LabeledPrice("Покупка фото",10*100)])

# Функция, отвечающая за раздел товаров
def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Товар #1')
    button2 = types.KeyboardButton('🔹 Товар #2')
    button3 = types.KeyboardButton('🔹 Товар #3')
    button4 = types.KeyboardButton('🔹 Товар #4')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел настроек
# Функция, отвечающая за раздел помощи
def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Раздел справки.\nЗдесь ты можешь написать моему разработчику.', reply_markup=markup)


def succes(message):
    global idPhoto
    if idPhoto == 1:
        bot.send_photo(message.chat.id, "https://postimg.cc/XpfdTBjG")
    if idPhoto == 2:
        bot.send_photo(message.chat.id, "https://postimg.cc/t1T6ZrhW")
    if idPhoto == 3:
        bot.send_photo(message.chat.id, "https://postimg.cc/hXKTg4vC")
    if idPhoto == 4:
        bot.send_photo(message.chat.id, "https://postimg.cc/LnKjC3pF")
    
# Строчка, чтобы программа не останавливалась
bot.polling(none_stop=True)