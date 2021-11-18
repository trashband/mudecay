import sqlite3
import time
import telebot
from telebot import types

event = {
    1 : {
      "VIP_time" : "23:50",
      "time" : "23:55",
      "name" : "CC  Selupan 14",
      "FullName" : "00:00 \nChaos Castle \nSelupan [до 14 ГР]",
      "img" : "eventimg/1sample-out.jpg"
    },
    2 : {
      "VIP_time" : "01:20",
      "time" : "01:25",
      "name" : "BC",
      "FullName" : "01:30 \nBlood Castle",
      "img" : "eventimg/2sample-out.jpg"
    },
    3 : {
      "VIP_time" : "01:50",
      "time" : "01:55",
      "name" : "DS Selupan 22",
      "FullName" : "02:00 \nDevil Square \nSelupan [до 22 ГР]",
      "img" : "eventimg/3sample-out.jpg"
    },
    4 : {
      "VIP_time" : "03:20",
      "time" : "03:25",
      "name" : "BC",
      "FullName" : "03:30 \nBlood Castle",
      "img" : "eventimg/4sample-out.jpg"
    },
    5 : {
      "VIP_time" : "03:50",
      "time" : "03:55",
      "name" : "Selupan 14",
      "FullName" : "04:00 \nSelupan [до 14 ГР]",
      "img" : "eventimg/5sample-out.jpg"
    },
    6 : {
      "VIP_time" : "04:35",
      "time" : "04:40",
      "name" : "DS",
      "FullName" : "05:00 \nDevil Square",
      "img" : "eventimg/6sample-out.jpg"
    },
    7 : {
      "VIP_time" : "05:00",
      "time" : "05:05",
      "name" : "Golden Invasion",
      "FullName" : "05:10 \nGolden Invasion",
      "img" : "eventimg/7sample-out.jpg"
    },
    8 : {
      "VIP_time" : "05:20",
      "time" : "05:25",
      "name" : "BC",
      "FullName" : "05:30 \nBlood Castle",
      "img" : "eventimg/8sample-out.jpg"
    },
    9 : {
      "VIP_time" : "05:50",
      "time" : "05:55",
      "name" : "Selupan 6",
      "FullName" : "06:00 \nSelupan [до 6 ГР]",
      "img" : "eventimg/9sample-out.jpg"
    },
    10 : {
      "VIP_time" : "07:20",
      "time" : "07:25",
      "name" : "BC",
      "FullName" : "07:30 \nBlood Castle",
      "img" : "eventimg/10sample-out.jpg"
    },
    11 : {
      "VIP_time" : "07:35",
      "time" : "07:40",
      "name" : "DS Selupan Amy",
      "FullName" : "08:00 \nDevil Square \nSelupan [любой ГР]",
      "img" : "eventimg/11sample-out.jpg"
    },
    12 : {
      "VIP_time" : "08:20",
      "time" : "08:25",
      "name" : "Meduse",
      "FullName" : "08:30 \nMedusa Event",
      "img" : "eventimg/12sample-out.jpg"
    },
    13 : {
      "VIP_time" : "08:50",
      "time" : "08:55",
      "name" : "Crywolf",
      "FullName" : "09:00 \nCrywolf Event",
      "img" : "eventimg/13sample-out.jpg"
    },
    14 : {
      "VIP_time" : "09:20",
      "time" : "09:25",
      "name" : "BC",
      "FullName" : "09:30 \nBlood Castle",
      "img" : "eventimg/14sample-out.jpg"
    },
    15 : {
      "VIP_time" : "09:50",
      "time" : "09:55",
      "name" : "CC Selupan 22",
      "FullName" : "10:00 \nChaos Castle \nSelupan [до 22 ГР]",
      "img" : "eventimg/15sample-out.jpg"
    },
    16 : {
      "VIP_time" : "10:35",
      "time" : "10:40",
      "name" : "DS Selupan Any",
      "FullName" : "11:00 \nDevil Square \nSelupan [любой ГР]",
      "img" : "eventimg/16sample-out.jpg"
    },
    17 : {
      "VIP_time" : "11:00",
      "time" : "11:05",
      "name" : "Gold Dragon",
      "FullName" : "11:10 \nGolden Invasion",
      "img" : "eventimg/17sample-out.jpg"
    },
    18 : {
      "VIP_time" : "11:20",
      "time" : "11:25",
      "name" : "BC",
      "FullName" : "11:30 \nBlood Castle",
      "img" : "eventimg/18sample-out.jpg"
    },
    19 : {
      "VIP_time" : "11:50",
      "time" : "11:55",
      "name" : "CC Selupan 14",
      "FullName" : "12:00 \nChaos Castle \nSelupan [до 14 ГР]",
      "img" : "eventimg/19sample-out.jpg"
    },
    20 : {
      "VIP_time" : "12:20",
      "time" : "12:25",
      "name" : "Jewel Storm",
      "FullName" : "12:30 \nJewel Storm",
      "img" : "eventimg/20sample-out.jpg"
    },
    21 : {
      "VIP_time" : "12:50",
      "time" : "12:55",
      "name" : "CC",
      "FullName" : "13:00 \nChaos Castle",
      "img" : "eventimg/21sample-out.jpg"
    },
    22 : {
      "VIP_time" : "13:20",
      "time" : "13:25",
      "name" : "BC",
      "FullName" : "13:30 \nBlood Castle",
      "img" : "eventimg/22sample-out.jpg"
    },
    23 : {
      "VIP_time" : "13:35",
      "time" : "13:40",
      "name" : "DS Selupan 6",
      "FullName" : "14:00 \nDevil Square \nSelupan [до 6 ГР]",
      "img" : "eventimg/23sample-out.jpg"
    },
    24 : {
      "VIP_time" : "14:50",
      "time" : "14:55",
      "name" : "CC",
      "FullName" : "15:00 \nChaos Castle",
      "img" : "eventimg/24sample-out.jpg"
    },
    25 : {
      "VIP_time" : "15:00",
      "time" : "15:05",
      "name" : "Gold Dragon",
      "FullName" : "15:10 \nGolden Invasion",
      "img" : "eventimg/25sample-out.jpg"
    },
    26 : {
      "VIP_time" : "15:20",
      "time" : "15:25",
      "name" : "BC",
      "FullName" : "15:30 \nBlood Castle",
      "img" : "eventimg/26sample-out.jpg"
    },
    27 : {
      "VIP_time" : "15:50",
      "time" : "15:55",
      "name" : "CC selupan Any",
      "FullName" : "16:00 \nChaos Castle \nSelupan [любой ГР]",
      "img" : "eventimg/27sample-out.jpg"
    },
    28 : {
      "VIP_time" : "16:40",
      "time" : "16:45",
      "name" : "DS",
      "FullName" : "17:00 \nDevil Square",
      "img" : "eventimg/28sample-out.jpg"
    },
    29 : {
      "VIP_time" : "17:20",
      "time" : "17:25",
      "name" : "BC",
      "FullName" : "17:30 \nBlood Castle",
      "img" : "eventimg/29sample-out.jpg"
    },
    30 : {
      "VIP_time" : "17:50",
      "time" : "17:55",
      "name" : "CC Selupan 22",
      "FullName" : "18:00 \nChaos Castle \nSelupan [до 22 ГР]",
      "img" : "eventimg/30sample-out.jpg"
    },
    31 : {
      "VIP_time" : "18:50",
      "time" : "18:55",
      "name" : "CC Selupan Any",
      "FullName" : "19:00 \nChaos Castle \nSelupan [любой ГР]",
      "img" : "eventimg/31sample-out.jpg"
    },
    32 : {
      "VIP_time" : "19:20",
      "time" : "19:25",
      "name" : "BC",
      "FullName" : "19:30 \nBlood Castle",
      "img" : "eventimg/32sample-out.jpg"
    },
    33 : {
      "VIP_time" : "19:35",
      "time" : "19:40",
      "name" : "DS Selupan 14",
      "FullName" : "20:00 \nDevil Square \nSelupan [до 14 ГР]",
      "img" : "eventimg/33sample-out.jpg"
    },
    34 : {
      "VIP_time" : "20:20",
      "time" : "20:25",
      "name" : "Jewel Storm",
      "FullName" : "20:30 \nJewel Storm",
      "img" : "eventimg/34sample-out.jpg"
    },
    35 : {
      "VIP_time" : "20:30",
      "time" : "20:35",
      "name" : "Happy 15 min",
      "FullName" : "20:40 \nHappy 15 Minutes",
      "img" : "eventimg/35sample-out.jpg"
    },
    36 : {
      "VIP_time" : "20:50",
      "time" : "20:55",
      "name" : "CC Crywolf",
      "FullName" : "21:00 \nChaos Castle \nCrywolf Event",
      "img" : "eventimg/36sample-out.jpg"
    },
    37 : {
      "VIP_time" : "21:00",
      "time" : "21:05",
      "name" : "Golden Invasion",
      "FullName" : "21:10 \nGolden Invasion",
      "img" : "eventimg/37sample-out.jpg"
    },
    38 : {
      "VIP_time" : "21:20",
      "time" : "21:25",
      "name" : "BC",
      "FullName" : "21:30 \nBlood Castle",
      "img" : "eventimg/38sample-out.jpg"
    },
    39 : {
      "VIP_time" : "21:50",
      "time" : "21:55",
      "name" : "CW Selupan Any",
      "FullName" : "22:00 \nChaos Castle \nSelupan [любой ГР]",
      "img" : "eventimg/39sample-out.jpg"
    },
    40 : {
      "VIP_time" : "22:10",
      "time" : "22:15",
      "name" : "Meduse Event",
      "FullName" : "22:20 \nMedusa Event",
      "img" : "eventimg/40sample-out.jpg"
    },
    41 : {
      "VIP_time" : "22:35",
      "time" : "22:40",
      "name" : "DS Selupan 6",
      "FullName" : "23:00 \nDevil Square \nSelupan [до 6 ГР]",
      "img" : "eventimg/41sample-out.jpg"
    },
    42 : {
      "VIP_time" : "23:20",
      "time" : "23:25",
      "name" : "BC",
      "FullName" : "23:30 \nBlood Castle",
      "img" : "eventimg/42sample-out.jpg"
    }
  }







bot = telebot.TeleBot("2031549691:AAEh_8atr0C0rpzC7tCMKzHbqd4OtUUnSKc", parse_mode=None)
conn = sqlite3.connect('database.db', check_same_thread=False)





markup = types.ReplyKeyboardMarkup(True,False)

itembtna = types.KeyboardButton('Уровень чара')
itembtnd = types.KeyboardButton('Рассылка On/Off')
itembtne = types.KeyboardButton('Настроки')
markup.row(itembtna)
markup.row(itembtnd, itembtne)


settingskey = types.ReplyKeyboardMarkup(True,False)

add_char = types.KeyboardButton('➕ Добавить чара')
admin_msg = types.KeyboardButton('😭 Написать Админу')
about_menu = types.KeyboardButton('⚠️ Информация о боте')
main_menu = types.KeyboardButton('🔙 Назад')
settingskey.row(add_char, admin_msg)
settingskey.row(about_menu)
settingskey.row(main_menu)

removekb = types.ReplyKeyboardMarkup(True,False)

remove_char = types.KeyboardButton('❌ Удалить')
removekb.row(remove_char)
removekb.row(main_menu)

def keyboar(id):
  deletechars = types.ReplyKeyboardMarkup(True,False)
  cursor = conn.execute("SELECT * FROM party")
  for i in cursor:
    if i[1] == id:
      add_char = types.KeyboardButton(str(i[0]) + ' ' + i[2])
      deletechars.row(add_char)
  back_char = types.KeyboardButton('🔙 Назад')
  deletechars.row(back_char)

  return deletechars

# def keyboar(id):
#   cursor = conn.execute("SELECT * FROM party")
#   for i in cursor:
#     if(i[1]) == id:
#       print(i[2])