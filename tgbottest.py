import telebot
from telebot import types, TeleBot

bot: TeleBot=telebot.TeleBot('5405896020:AAHs3pgYf3bPhDohNxSzKKikcyX8K43jyIU')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет,как я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или как дела?")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.from_user.id, "у меня все хорошо, а у тебя?")
        if message.test == "хорошо":
            bot.send_message(message.from_user.id, "Здорово, я рад за тебя!")
        elif message.text == "плохо":
            bot.send_message(message.from_user.id, "Оу, как помочь тебе его поднять?")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


bot.polling(none_stop=True, interval=0)