# from telebot import*
# from telebot import types
# import sqlite3

# token = '6161308776:AAF1gURKAogJ-zF44fC3RM4W03sg2Qv6154' # Это токен бота для тестов
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def button(message):
    
#     chat_id = message.chat.id
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     bt1 = types.KeyboardButton('Показати клієнтів')

#     markup.add(bt1)
#     bot.send_message(chat_id, f'<b>Привіт {message.from_user.first_name}👋!</b> <b>Що бажаєш обрати?</b>',
#         parse_mode='html', reply_markup=markup)
    
# @bot.message_handler(content_types=['text'])
# def main(message):
#     chat_id = message.chat.id
#     conn = sqlite3.connect('instance/client.db')
#     cur = conn.cursor()
#     if message.chat.type == 'private':
#         if message.text == 'Показати клієнтів':
#             cur.execute('SELECT username, number FROM user')
#             users = cur.fetchall()
#             print(users )

#             info = ''
#             for el in users:
#                 info += f"Ім'я: {el[0]}\n Номер: {el[1]}\n \n"

#             bot.send_message(chat_id, info )

    

# if __name__ == '__main__':
#     bot.polling(none_stop=True, interval=0) 


import telebot
from telebot import time, types
from datetime import datetime, timedelta
from time import sleep
import sqlite3


clickIdTimes = {}
promocode = ['mafia', 'l1nkooln']

def checkClick(chat_id, timer_dict, timeout):
    if chat_id not in timer_dict or timer_dict[chat_id] < datetime.now() - timedelta(seconds=timeout):
        timer_dict[chat_id] = datetime.now()
        return True
    return False


print(checkClick(10, clickIdTimes, timeout=1))
print(checkClick(10, clickIdTimes, timeout=1))
sleep(2)
print(checkClick(10, clickIdTimes, timeout=1))
print(checkClick(10, clickIdTimes, timeout=1))

def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

light = '''Хімчистка салону (Light)

Седан: від 2000 грн
Джип (і більше): від 2500 грн

Комплекс робіт:
-> Чистка ковроліну
-> Чистка сидінь
-> Чистка дверних карт
-> Багажний відділ
-> Торпеда
-> Стеля'''

hard = '''Хімчистка салону (Hard)

Седан: від 2800 грн
Джип (і більше): від 3500 грн

Комплекс робіт:
-> Опція (Light)
-> Демонтаж сидінь
-> Чистка важкодоступних місць
-> Чистка ущільнювачів
-> Чистка вікон
-> Мийка дверних стійок
-> Обробка кондиціонером/поліроль для пластику
Чистка окремих елементів від 300 гривень'''

somet = '''
-------------------------------------------
Мийка авто: від 300 грн
Нанесення воску: від 300 грн
Нанесення захистного покриття: від 600 грн
Нанесення антидощу: від 800 грн
Нанесення керамічного покриття: від 150$
-------------------------------------------
Оптика:
Бронювання оптики: від 800 грн
Полірування фар: від 600 грн (за пару)
Тонування фар: від 600 грн (за пару)
-------------------------------------------
Плівочні роботи:
Поклейка авто плівкою в круг (кольорова/бронеплівка): від 600$
Поклейка авто плівкою за елемент (кольорова/бронеплівка): від 75$'''

token = '5534255353:AAEtoH_e2PTrvrP1D1MCSCJaM5ntbcLwqnc' # Это токен бота для тестов
bot = telebot.TeleBot(token)
admin_id = (1132004570) # ID Админов которые будут получать заявки
global user_name
global user_phone
# 1090256518 - Влад
# 1132004570 - My

@bot.message_handler(commands=['start'])
def button(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # bt1 = types.KeyboardButton('⏰Записатися на хімчистку')
    bt3 = types.KeyboardButton('💻Розробник')
    # bt4 = types.KeyboardButton('📍📞Контактна адреса')
    bt5 = types.KeyboardButton('💰Прайс')
    bt6 = types.KeyboardButton('📬Меню запису')
    bt7 = types.KeyboardButton('🔔Залишити відгук')
    markup.add(bt5, bt6, bt7, bt3)
    admins_id = [1090256518, 1132004570]
    for admin in admins_id:
        if message.from_user.id == admin:
            bt8 = types.KeyboardButton('Показати клієнтів')
            markup.add(bt8)
        else:
            pass
    bot.send_message(chat_id, f'<b>Привіт {message.from_user.first_name}👋!</b> <b>Що бажаєш обрати?</b>',
        parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':

        # if message.text == '⏰Записатися на хімчистку':
        #     msg = bot.send_message(chat_id, "Напиши свій ПІБ")
        #     bot.register_next_step_handler(msg,regist_1)
        if message.text == '💻Розробник':
            bot.send_message(chat_id, '@l1nkoooln')
        elif message.text == '💰Прайс':
            bot.send_message(chat_id, light)
            bot.send_message(chat_id, hard)
            bot.send_message(chat_id, somet)
        elif message.text == '🔔Залишити відгук':
                vid = bot.send_message(chat_id, 'Напиши свій ПІБ:')
                bot.register_next_step_handler(vid, vidguk)
        elif message.text == 'Показати клієнтів':
            conn = sqlite3.connect('instance/client.db')
            cur = conn.cursor()
            cur.execute('SELECT username, number FROM user')
            users = cur.fetchall()
            print(users)
            info = ''
            for el in users:
                info += f"Ім'я: {el[0]}\n Номер: {el[1]}\n \n"

            bot.send_message(chat_id, info )

        elif message.text == '📍📞Контактна адреса':
            bot.send_message(chat_id, '📞Контакти: \n 0994766635 - Влад \n 0965786006 - Іван \n 📍Вул. Жовківська 14 (Завод РЕМА).Львів')
        elif message.text == '📬Меню запису':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('⏰Записатися на хімчистку')
            # item2 = types.KeyboardButton('📍📞Контактна адреса')
            back = types.KeyboardButton('⬅️У головне меню')
            markup.add(item1, back)
            bot.send_message(message.chat.id, '📬Меню запису', reply_markup=markup)

        elif message.text == '⏰Записатися на хімчистку':
            a = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, 'Что', reply_markup=a)
            if not checkClick(chat_id, clickIdTimes, 30*60):
                bot.send_message(chat_id, "📌Ви вже записалися \n Спробуйте пізніше")
                return
            msg = bot.send_message(chat_id, "Напиши свій ПІБ")
            bot.register_next_step_handler(msg,regist_1)
        elif message.text == '📍📞Контактна адреса':
            bot.send_message(chat_id, '📞Контакти: \n 0994766635 - Влад \n 0965786006 - Іван \n 📍Вул. Жовківська 14 (Завод РЕМА).Львів')
        elif message.text == '⬅️У головне меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # bt1 = types.KeyboardButton('⏰Записатися на хімчистку')
            bt3 = types.KeyboardButton('💻Розробник')
            # bt4 = types.KeyboardButton('📍📞Контактна адреса')
            bt5 = types.KeyboardButton('💰Прайс')
            bt6 = types.KeyboardButton('📬Меню запису')
            bt7 = types.KeyboardButton('🔔Залишити відгук')
            markup.add(bt3,  bt5, bt6, bt7)
            bot.send_message(message.chat.id, '⬅️У головне меню', reply_markup=markup)

def vidguk(message):
    global name
    global vid3
    name = message.text
    vid2 = bot.send_message(message.chat.id, 'Поставь свою оцінку від 0-10 :)')
    bot.register_next_step_handler(vid2, vidguk2)
def vidguk2(message):
    global name
    global vid3
    vid3 = message.text
    bot.send_message(message.chat.id, '📌Дякую за відгук :)')
    bot.send_message(admin_id, f"📍 Новий відгук :)\nНік юзера: {message.from_user.username} \nІм'я: {name} \nОцінка: {vid3}")
def regist_1(message):
    global user_name
    global msg3
    global name
    global vid3
    user_name = message.text
    msg3 = bot.send_message(message.chat.id, "📞Напиши свій номер телефону для зв'язку.\n(Наш менеджер тобі передзвонить для уточнення інформації)")
    bot.register_next_step_handler(msg3, regist_2)
def regist_2(message):
    global user_phone
    global user_name
    global kyzov
    global msg3
    global user_phone_2
    global name
    global vid3
    user_phone = message.text
    msg2 = bot.send_message(message.chat.id, "🧽Який кузов т/з на якому буде проводитися роботи?\n (Седан, універсал, бус, інше...)")
    bot.register_next_step_handler(msg2, regist_3)

def regist_3(message):
    global user_phone
    global user_name
    global kyzov
    global msg3
    global user_phone_2
    global name
    global vid3
    kyzov = message.text
    msg4 = bot.send_message(message.chat.id, "📎Введіть промокод: \nЯкщо немає, напишіть : - ")
    bot.register_next_step_handler(msg4, regist_4)
def regist_4(message):
    global user_phone
    global user_name
    global kyzov
    global promo
    global name
    global vid3
    promo = message.text
    if promo in promocode:
        bot.send_message(message.chat.id, '📌Промокод прийнято :) \n Активовано 20% знижку :)')
    elif promo =='-':
        promo = '-'
    else:
        bot.send_message(message.chat.id, '📌Промокод не знайдено або він прострочений :(')
        promo = '-'

    bot.send_message(message.chat.id,"🗓Дякую, ваша заявка прийнята і буде передана спеціалістам. Очікуйте дзвінка")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, f'<b>Привіт {message.from_user.first_name}👋!</b> <b>Що бажаєш обрати?</b>',
        parse_mode='html', reply_markup=markup)
    bot.send_message(admin_id, f"📍Нова заявка: \n Нік юзера: {message.from_user.username} \n ПІБ: {user_name}\n Номер телефону: {user_phone} \n Кузов т/з: {kyzov} \n Промокод: {promo}")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

