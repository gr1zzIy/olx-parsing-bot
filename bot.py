import cfg, telebot, time
from pars import *
from telebot import types

bot = telebot.TeleBot(cfg.API_TOKEN)

@bot.message_handler(commands="hi")
def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["sosat`", "+", "lezhat`"]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, f"<b>Вассап {message.from_user.first_name}!</b>", parse_mode='html', reply_markup=keyboard)


# @bot.message_handler(commands="mq")
# def mq(message: types.Message):

#     title = str(old_new())

#     if title == "new":
#         title = str(get_title())
#         price = str(get_price())
#         photo = get_img()
#         link = get_link()
#         caption = f"Назва: \n       {title} \nЦіна: \n      {price}\nПосилання: \n      {link}"
#         bot.send_photo(message.chat.id, photo, caption)
#     else:
#         bot.send_message(message.chat.id, "sosat`")
#     #bot.send_message(message.chat.id, get_title())

@bot.message_handler(content_types="text")
def start(message):

    beneficent = "https://www.olx.ua/"

    url = message.text
    bot.send_message(message.chat.id, url)
    if beneficent in url:
        
        while True:

            title = str(old_new(url))

            if title == "new":
                title = str(get_title(url))
                price = str(get_price(url))
                photo = get_img(url)
                link = get_link(url)
                caption = f"Назва: \n       {title} \nЦіна: \n      {price}\nПосилання: \n      {link}"
                bot.send_photo(message.chat.id, photo, caption)
            else:
                bot.send_photo(message.chat.id, "wait")
                time.sleep(30)

            time.sleep(30)
            
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            print(ex)