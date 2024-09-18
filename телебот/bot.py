# import telebot 
# from time import sleep



# token='6705626249:AAE776ZbWNI7EJ356UkEn0FIw0M0uio4RxU'
# bot = telebot.TeleBot(token)



# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет я бот. Чем могу помочь')
    
# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.from_user.id, 'Привет, хочешь узнать топ моих любимых аниме?')
#     elif message.text == 'Да конечно':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'ВОТ: 1 ДЖО ДЖО 2 ХАНТЕР Х ХАНТЕР 3 ВАН ПИС 4 БЛИЧ 5 ЧЕРНЫЙ КЛЕВЕР')
#     elif message.text == 'Круто скинь еще лубимые музыки':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'ХЗ у меня мало времени')
#     else:
#         bot.send_message(message.from_user.id, 'жосска')
        
# bot.infinity_polling()
