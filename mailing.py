import sys
import time
import datetime
import telebot
import mysql.connector
import calendar

from telebot import types
from datetime import date

bot = telebot.TeleBot("1589987650:AAFmyj_ZuvViGQQdhWBGW6y8raCY_zEzlaM")

try:
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root",
      port="3306",
      database="prac"
    )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    sys.exit()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    sys.exit()
  else:
    print(err)
    sys.exit()

cursor = db.cursor()

now = datetime.datetime.now()
timing = time.time()
while True:
    if time.time() - timing > 3600.0:
        timing = time.time()
        if now.hour==8 and now.minute==0:
            sql = "SELECT id FROM users WHERE accpet = %s "
            val = (1, )
            cursor.execute(sql, val)
            userss = cursor.fetchall()
            for user1 in userss:
                print(user1[0])
                my_date = date.today()
                today = calendar.day_name[my_date.weekday()]
                user_id = user1[0]
                if today == 'Monday':
                    bot.send_message(user1[0], "Расписание на сегодня:")
                    sql = "SELECT \
                        classes.Monday AS class \
                        FROM users\
                        INNER JOIN classes ON users.class = classes.id AND users.id = %s "
                    val = (user_id, )
                    cursor.execute(sql, val)
                    users = cursor.fetchall()
                    for user in users:
                        bot.send_message(user1[0], user[0])
                        print(user[0])
                #---------------------------------------------------------------------------
                elif today == 'Tuesday':
                    bot.send_message(user1[0], "Расписание на сегодня:")
                    sql = "SELECT \
                        classes.Tuesday AS class \
                        FROM users\
                        INNER JOIN classes ON users.class = classes.id AND users.id = %s "
                    val = (user_id, )
                    cursor.execute(sql, val)
                    users = cursor.fetchall()
                    for user in users:
                        bot.send_message(user1[0], user[0])
                        print(user[0])
                #---------------------------------------------------------------------------
                elif today == 'Wednesday':
                    bot.send_message(user1[0], "Расписание на сегодня:")
                    sql = "SELECT \
                        classes.Wednesday AS class \
                        FROM users\
                        INNER JOIN classes ON users.class = classes.id AND users.id = %s "
                    val = (user_id, )
                    cursor.execute(sql, val)
                    users = cursor.fetchall()
                    for user in users:
                        bot.send_message(user1[0], user[0])
                        print(user[0].split(', '))
                #---------------------------------------------------------------------------
                elif today == 'Thursday':
                    bot.send_message(user1[0], "Расписание на сегодня:")
                    sql = "SELECT \
                        classes.Thursday AS class \
                        FROM users\
                        INNER JOIN classes ON users.class = classes.id AND users.id = %s "
                    val = (user_id, )
                    cursor.execute(sql, val)
                    users = cursor.fetchall()
                    for user in users:
                        bot.send_message(user1[0], user[0])
                        print(user[0])
                #---------------------------------------------------------------------------   
                elif today == 'Friday':
                    bot.send_message(user1[0], "Расписание на сегодня:")
                    sql = "SELECT \
                        classes.Friday AS class \
                        FROM users\
                        INNER JOIN classes ON users.class = classes.id AND users.id = %s "
                    val = (user_id, )
                    cursor.execute(sql, val)
                    users = cursor.fetchall()
                    for user in users:
                        bot.send_message(user1[0], user[0])
                        print(user[0])
                else:
                    bot.send_message(user1[0], "Сегодня выходной")
                db.commit()
            db.commit()
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)