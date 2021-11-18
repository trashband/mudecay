import telebot
from telebot import types
import time
import sqlite3
import func

bot = telebot.TeleBot("2031549691:AAEh_8atr0C0rpzC7tCMKzHbqd4OtUUnSKc", parse_mode=None)
conn = sqlite3.connect('database.db', check_same_thread=False)

i=0
while True:
    while i <= 42:
        named_tuple = time.localtime() # получить struct_time
        time_string = time.strftime("%H:%M", named_tuple)
        i += 1

        # VIP Notice
        if(time_string == func.event[i]["VIP_time"]):
            cursor = conn.execute("SELECT * FROM user")

            for val in cursor:
                if (val[3] == 1) and (val[4] == 1):
                    try:
                        j = i + 1
                        if(j == 43):
                            j = 1
                        event = func.event[i]["FullName"] + '\n\nСледующий:\n\n' + func.event[j]["FullName"]
                        bot.send_photo(val[1], open('eventimg/'+ str(i) + 'sample-out.jpg', 'rb'), caption=event)
                        print('Уведомления отправленны ')
                    except Exception as e:
                        print(e)

            time.sleep(60)


        # Normal Notice
        if(time_string == func.event[i]["time"]):
            cursor = conn.execute("SELECT * FROM user")

            for val in cursor:
                if (val[3] == 1) and (val[4] == 0):
                    try:
                        helpmsg = "\n\n - Поддержи проект. Оформи VIP-bot всего за 5 Jewel Decay за неделю! \n 🤟 Пиши в игре на ник SmilePanda 🤟"
                        bot.send_photo(val[1], open('eventimg/'+ str(i) + 'sample-out.jpg', 'rb'), caption=func.event[i]["FullName"] + helpmsg)
                        print('Уведомления отправленны ')
                    except Exception as e:
                        print(e)

            time.sleep(60)
        if(i == 42):
            i = 0
        time.sleep(0.2)









# event_timer = conn.execute("SELECT * FROM event_timer")
# cursor = conn.execute("SELECT * FROM user")

# db_list = []
# while True:
#     named_tuple = time.localtime() # получить struct_time
#     time_string = time.strftime("%H:%M", named_tuple)

#     for db_name in conn.execute("SELECT * FROM event_timer"):
#         db_list.append(db_name)

#     for ev in db_list:
#         time.sleep(0.1)
#         if(time_string == ev[1]):
#             for val in cursor:
#                 if val[3] == 1:
#                     try:
#                         bot.send_photo(val[1], open(ev[4], 'rb'), caption=ev[2])
#                         print('Уведомления отправленны ')
#                     except Exception as e:
#                         print(e)            

#     time.sleep(0.2)

