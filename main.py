import random
from PIL import Image, ImageDraw, ImageFont
import telebot
token="5954530100:AAGUkVKnI-iJXspRGG-BIqNBiwdMRYfpddo"
#step2
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привіт ✌\nнадішли фоточку в форматі png/jpeg, щоб створити мем")
# step3 отримання повідомлення від юзера фото
@bot.message_handler(content_types=['photo'])
def photo(message):
    #print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    #print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    #print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file) #збереження як файлу
    # список мемчиків зберігається в текстовому файлі
    f = open('meme.txt', 'r', encoding='UTF-8')
    meme = f.read().split('\n')
    f.close()
    image = Image.open("image.jpg")

    font = ImageFont.truetype("arial", 45)
    drawer = ImageDraw.Draw(image)

    width, height = image.size
    print(width, height)
    drawer.text((150, height // 1.2), random.choice(meme), font=font, fill='white')

    image.save('new_img.jpg')
    #image.show()
    bot.send_photo(message.chat.id, open('new_img.jpg', 'rb'))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Та фото мені кидай)')
#запуск бота(обов'язково)
bot.polling()
