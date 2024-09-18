
import telebot
import requests
import re
import subprocess
import os

# Замените 'your_token_here' на свой токен
token = '7427510298:AAGL-L2ofKB2xKPUkhNiAMzpeRZ1ThNDorA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь мне ссылку на видео TikTok, и я помогу тебе его скачать.")

@bot.message_handler(content_types=['text'])
def download_tiktok_video(message):
    url = message.text.strip()
    
    # Проверяем, является ли введённый текст ссылкой на TikTok
    if 'tiktok.com' in url:
        try:
            # Используем youtube-dl для скачивания видео 
            # Подготовим команду
            out_file = 'video.mp4'
            command = ['youtube-dl', url, '-o', out_file]
            subprocess.run(command, check=True)

            # Отправим скачанное видео пользователю
            with open(out_file, 'rb') as video:
                bot.send_video(message.chat.id, video)

            # Удалим файл после отправки
            os.remove(out_file)
        except Exception as e:
            bot.send_message(message.chat.id, f'Ошибка скачивания: {str(e)}')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте корректную ссылку на видео TikTok.')

bot.polling()