import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import sqlite3
import func

import time
import parser

from function import answer, char, keyboard, user

bot = telebot.TeleBot("2031549691:AAEh_8atr0C0rpzC7tCMKzHbqd4OtUUnSKc", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	answer = "Информационный бот сервера MuDecay.ru.\n - Оповещение о начале квестов (BC, DS, CC...).\n - Включение и отключение уведомлений! \n - Проверка lvl персонажа.\n - Информация о новых товарах на форуме (В процессе).\n --------- VIP Bonus -------------\n - Оповешение про квест за 5 минут до начала и информация про следующий квест (для VIP).\n - Оповещение о резете персонажа (для VIP)."
	bot.send_photo(message.from_user.id, open('titlebg.jpg', 'rb'), caption = answer,reply_markup=func.markup)
	# bot.reply_to(message, "Информационный бот сервера MuDecay.ru.\n - Оповещение о начале квестов (BC, DS, CC...).\n - Проверка lvl персонажа (В процессе).\n - Информация о новых товарах на форуме (В процессе).",reply_markup=func.markup)
	user.add_user(message.from_user.id, message.from_user.first_name)
	print (user.user_data(message.from_user.id))

@bot.message_handler(content_types=["text"])
def get_message(message):
	if message.text == 'Уровень чара':
		try:
			info = 'Ник: ' + str(char.char_name(message.from_user.id)[2]) + '\n' + 'Уровень: ' + str(char.char_name(message.from_user.id)[4]) + '\n' + 'Резет: ' + str(char.char_name(message.from_user.id)[5]) + '\n' +'Класс: ' + str(char.char_name(message.from_user.id)[3] + '\n\n - Поддержи проект. Оформи VIP-bot всего за 5 Jewel Decay за неделю! \n 🤟 Пиши в игре на ник SmilePanda 🤟') 
			bot.reply_to(message, info,reply_markup=gen_markup())
		except Exception as e:
			info = 'Вы не добавили персонажа!'
			bot.reply_to(message, info,reply_markup=func.settingskey)
	if message.text == '⚠️ Информация о боте':
		answer = "Информационный бот сервера MuDecay.ru.\n - Оповещение о начале квестов (BC, DS, CC...).\n - Включение и отключение уведомлений! \n - Проверка lvl персонажа.\n - Информация о новых товарах на форуме (В процессе).\n --------- VIP Bonus -------------\n - Оповешение про квест за 5 минут до начала и информация про следующий квест (для VIP).\n - Оповещение о резете персонажа (для VIP)."
		bot.reply_to(message, answer,reply_markup=func.markup)
	if message.text == 'Рассылка On/Off':
			if (user.user_data(message.from_user.id)[0][3] == 1):
				bot.reply_to(message, 'Вы отписались от уведомлений',reply_markup=func.markup)
				user.notics_stat(message.from_user.id, 0)
			else:
				bot.reply_to(message, 'Вы подписались на уведомления',reply_markup=func.markup)
				user.notics_stat(message.from_user.id, 1)
	if message.text == 'Настроки':
			bot.reply_to(message, 'Меню настроек 👻',reply_markup=func.settingskey)
	if message.text == '➕ Добавить чара':
			bot.reply_to(message, 'Введите ник персонажа 👻 \n- Бот показывает информацию только о первом добавленном чаре! Для контроля пачьки из 5 персонажей приобретите VIP bot',reply_markup=func.settingskey)
			bot.register_next_step_handler(message,add_characters)
	if message.text == '😭 Написать Админу':
			bot.reply_to(message, 'Введите текс обращения!',reply_markup=func.settingskey)
			bot.register_next_step_handler(message,msg_to_admin)
	if message.text == '🔙 Назад':
			bot.reply_to(message, 'Главное меню',reply_markup=func.markup)

def add_characters(message):
    bot.send_message(message.chat.id,message.text + ' успешно добавлен!🤟 \n Бот показывает информацию только о первом добавленном чаре! Для контроля пачьки из 5 персонажей приобретите VIP bot',reply_markup=func.markup)
    char.add_char1(message.from_user.id, message.text, 'non', 0, 0)
def msg_to_admin(message):
    bot.send_message(message.chat.id,'Сообщение отправленно!',reply_markup=func.markup)
    answer.push_to_base(message.from_user.id, message.text)
def delete_char(message):
    answer = message.text.split(' ')
    char.delete_char(answer[0], message.from_user.id)
    bot.send_message(message.chat.id,'Ты добровольно ликвидирова из базы персонажа ' + answer[1],reply_markup=func.markup)

# Inline Keyboard

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Удаление персонажей", callback_data="cb_yes"))
    # markup.add(InlineKeyboardButton("Удалить", callback_data="cb_yes"),
    #                            InlineKeyboardButton("Изменить", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        # bot.answer_callback_query(call.id, "Меню удаления персонажа")
        bot.send_message(call.from_user.id, "Меню удаления персонажа", reply_markup=func.keyboar(call.from_user.id))
        bot.register_next_step_handler(call.message, delete_char)
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "В данный момент функция не доступна!")

bot.infinity_polling()