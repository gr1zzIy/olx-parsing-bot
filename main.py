import cfg, asyncio, logging, time
from pars import *
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types


# задаем уровень логов
logging.basicConfig(level=logging.INFO)


bot = Bot(token=cfg.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types="text")
async def url_write(message):

    beneficent = "https://www.olx.ua/"
    url = message.text

    if beneficent in url:
        with open("url.txt", "w", encoding='utf-8') as f:
            f.write(url)

@dp.message_handler(content_types="text")
async def delay(wait):
    
    while True:
        await asyncio.sleep(wait)

        url = []
        file = open("url.txt", encoding='utf-8')
        url = str(file.read())

        title = str(old_new(url))

        if title == "new":
            title = str(get_title(url))
            price = str(get_price(url))
            photo = get_img(url)
            link = get_link(url)
            caption = f"Назва: \n       {title} \nЦіна: \n      {price}\nПосилання: \n      {link}"
            await bot.send_photo(724700370, photo, caption)
        else:
            time.sleep(30)


# async def delay(wait_for):
#     while True:
#         await asyncio.sleep(wait_for)

#         now = datetime.utcnow()
#         await bot.send_message(724700370, f"{now}", disable_notification = True)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(delay(10)) # пока что оставим 10 секунд (в качестве теста)
    executor.start_polling(dp, skip_updates=True)