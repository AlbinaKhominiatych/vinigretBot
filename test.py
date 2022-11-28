import telebot

TOKEN = '5954530100:AAGUkVKnI-iJXspRGG-BIqNBiwdMRYfpddo'

tb = telebot.TeleBot(TOKEN) #create a new Telegram Bot object
chat_id =1880672393

foto = open('new_img.jpg', 'rb')
tb.send_photo(chat_id, foto)
tb.polling()