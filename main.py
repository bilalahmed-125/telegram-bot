from telebot import types
import telebot

token = '1477712752:AAGoOvvQEBYgdZLzq8IIgGh3TLj5HQpT_5w'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    print(message)

    if text == 'hi':
        bot.send_message(chat_id, "Hi, Bot is here")
    if text == 'how are you?':
        bot.send_message(chat_id, "I'm fine sir and how are you.")
    if text == 'ask my age.':
        chat_id = message.chat.id
        text = message.text
        msg = bot.send_message(chat_id, 'How old are you?')
        bot.register_next_step_handler(msg, askAge)

def askAge(message):
    chat_id = message.chat.id
    text = message.text

    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Age must be a number, enter again.')
        bot.register_next_step_handler(msg, askAge)
    else:
        msg = bot.send_message(chat_id, 'Thank you I remembered that you are' + text + 'yo.')


@bot.message_handler(content_types=['video'])
def video_handler(message):
    bot.send_message(message.chat.id, 'beautiful video')
source_markup = types.ReplyKeyboardMarkup(row_width=6, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Start')
source_markup_btn2 = types.KeyboardButton('End')
source_markup.add(source_markup_btn1, source_markup_btn2,source_markup_btn1,source_markup_btn2)

new_source_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_1 = types.KeyboardButton('Button 1')
btn_2 = types.KeyboardButton('Button 2')
btn_3 = types.KeyboardButton('Button 3')
btn_4 = types.KeyboardButton('Button 4')
btn_5 = types.KeyboardButton('Button 5')
btn_6 = types.KeyboardButton('Button 6')
new_source_markup.row(btn_1, btn_2)
new_source_markup.row(btn_3, btn_4, btn_5, btn_6)
@bot.message_handler(func=lambda message: True, content_types=['text'])
def start_handler(message):
    if message.text == "/start":
       msg = bot.reply_to(message, text="hi", reply_markup=new_source_markup)
    print(message.text)


bot.polling()
