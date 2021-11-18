import time
import requests
from bs4 import BeautifulSoup
from function import user, char

import telebot
from telebot import types

import sqlite3

bot = telebot.TeleBot("2031549691:AAEh_8atr0C0rpzC7tCMKzHbqd4OtUUnSKc", parse_mode=None)
conn = sqlite3.connect('database.db', check_same_thread=False)





while True:
    i = -1
    while i <= len(char.char_list()):
        i += 1
               


        try:
            url = 'https://www.mudecay.ru/?character=' + str(char.char_list()[i][2])
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find('center', class_= 'resetchar')
            arr = {
                'lvlchar' : soup.find('center', class_= 'lvlchar').text if result else "0", 
                'racechar' : soup.find('center', class_= 'racechar').text, 
                'namechar' : soup.find('center', class_= 'namechar').text, 
                'resetchar' : soup.find('center', class_= 'resetchar').text if result else "0", 
                # 'grchar' : soup.find('center', class_= 'grchar').text if result else "0", 
                'lastenterchar' : soup.find('center', class_= 'lastenterchar').text
            }            
        except Exception as e:
            print(e)



        data1 = (str(arr['racechar']), int(arr['lvlchar']), int(arr['resetchar']), str(arr['namechar']))


        sql_update = ''' UPDATE party 
        SET race=?, lvl=?, reset=?
        WHERE slot_1=?
        '''
        try:
            cursor = conn.cursor()
            cursor.execute(sql_update, data1)
            conn.commit()
        except Exception as e:
            print(e)
        finally: 
            print('Execute Update SQL successfully.')

        # Отправка сообщения если персонаж 400 лвл
        if (arr['lvlchar'] == "400"):
            if(user.user_data(char.char_list()[i][1])[0][4] == 1) and (user.user_data(char.char_list()[i][1])[0][3] == 1) and (char.char_list()[i][6] == 0):
                char.upd_flag(arr['namechar'], 1)
                bot.send_message(char.char_list()[i][1], 'Чар подгорает без резета! \n ' + char.char_list()[i][2] + ' уже 400 лвл')
                print(user.user_data(char.char_list()[i][1])[0][2] + " Сделай паскуда резет!")
        elif(arr['lvlchar'] <= "399"):
            char.upd_flag(arr['namechar'], 0)

        print(arr)

        if i == len(char.char_list()) - 1:
            i=-1
            time.sleep(250)
        time.sleep(1)
