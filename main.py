import random
import asyncio
import aiohttp
from PIL import Image, ImageDraw, ImageFont
from aiogram import Bot, Dispatcher, types

token = "5954530100:AAGUkVKnI-iJXspRGG-BIqNBiwdMRYfpddo"

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply("Привіт ✌\nнадішли фоточку в форматі png/jpeg, щоб створити мем")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def process_photo(message: types.Message):
    photo = message.photo[-1]

    # Отримання файлу зображення
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path

    # Отримання URL файлу зображення
    file_url = bot.get_file_url(file_path)

    # Завантаження файлу зображення
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status == 200:
                image_data = await response.read()

                with open("image.jpg", 'wb') as new_file:
                    new_file.write(image_data)

                # Список мемчиків зберігається в текстовому файлі
                with open('meme.txt', 'r', encoding='UTF-8') as f:
                    meme = f.read().split('\n')

                image = Image.open("image.jpg")

                font = ImageFont.truetype("arial", 45)
                drawer = ImageDraw.Draw(image)

                width, height = image.size
                drawer.text((150, height // 1.2), random.choice(meme), font=font, fill='white')

                image.save('new_img.jpg')

                # Відправлення нового зображення
                with open('new_img.jpg', 'rb') as new_image:
                    await message.reply_photo(new_image)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    await message.reply('Та фото мені кидай)')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(dp.start_polling())
    finally:
        loop.close()
