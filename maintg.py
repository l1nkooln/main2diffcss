from telebot import*
from telebot import types
import sqlite3

token = '6161308776:AAF1gURKAogJ-zF44fC3RM4W03sg2Qv6154' # Это токен бота для тестов
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def button(message):
    
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Показати клієнтів')

    markup.add(bt1)
    bot.send_message(chat_id, f'<b>Привіт {message.from_user.first_name}👋!</b> <b>Що бажаєш обрати?</b>',
        parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id
    conn = sqlite3.connect('instance/client.db')
    cur = conn.cursor()
    if message.chat.type == 'private':
        if message.text == 'Показати клієнтів':
            cur.execute('SELECT username, number FROM user')
            users = cur.fetchall()
            print(users )

            info = ''
            for el in users:
                info += f"Ім'я: {el[0]}\n Номер: {el[1]}\n \n"

            bot.send_message(chat_id, info )

    

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0) 