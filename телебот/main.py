import telebot

token = '6705626249:AAE776ZbWNI7EJ356UkEn0FIw0M0uio4RxU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('DIOR помада ') 
    button2 = telebot.types.KeyboardButton('DIOR духа')
    button3 = telebot.types.KeyboardButton('DIOR платье')
    button4 = telebot.types.KeyboardButton('DIOR реклама')
    button5 = telebot.types.KeyboardButton('DIOR очка')
    keyboard.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, "Welcome to my shopping bot! Please choose an option:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'DIOR помада ')
def send_lipstick(message):
    with open('350x350.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the DIOR lipstick. Nice!")

@bot.message_handler(func=lambda message: message.text == 'DIOR духа')
def send_perfume(message):
    with open('images.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the DIOR perfume. Nice!")        

@bot.message_handler(func=lambda message: message.text == 'DIOR платье')
def send_video_dress(message):
    with open('IMG_6397.MOV', 'rb') as vid:
        bot.send_video(message.chat.id, vid, caption="Это видео с платьем.")

@bot.message_handler(func=lambda message: message.text == 'DIOR реклама')
def send_ad(message):
    bot.send_message(message.chat.id, "Вот реклама DIOR!")

@bot.message_handler(func=lambda message: message.text == 'DIOR очка')
def send_sunglasses(message):
    # Убедитесь, что вы загружаете аудиофайл, а не изображение
    with open('audio_file.ogg', 'rb') as audio:  # Используйте корректный аудиофайл
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")

bot.polling()