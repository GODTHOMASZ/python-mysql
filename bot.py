import sys
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

#----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
        msg = bot.send_message(message.chat.id, 'Вас приветствует Чат-Бот "Ученик". Для регистрации введите свои ФИО в формате: Фамилия И.О.')
        bot.register_next_step_handler(msg, process_name_step)
        

def process_name_step(message):
    try:
        user_id = message.from_user.id
        sql = "UPDATE users SET id = %s WHERE name = %s"
        val = (user_id, message.text)
        cursor.execute(sql, val)
        db.commit()
        print('Запись обновлена!')
        bot.send_message(message.chat.id, "Вы успешно зарегистрированы!")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Расписание на сегодня")
        item2 = types.KeyboardButton("Расписание на неделю")
        item3 = types.KeyboardButton("Расписание звонков")
        item4 = types.KeyboardButton("Рассылка расписания")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Выберите команду.",
        parse_mode='html', reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'Ошибка. Такого ученика не существует или вы уже зарегистрированы!')
#----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == 'Включить':
          user_id = message.from_user.id
          sql = "UPDATE users SET accpet = %s WHERE id = %s"
          val = (1, user_id)
          cursor.execute(sql, val)
          db.commit()
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          item1 = types.KeyboardButton("Расписание на сегодня")
          item2 = types.KeyboardButton("Расписание на неделю")
          item3 = types.KeyboardButton("Расписание звонков")
          item4 = types.KeyboardButton("Рассылка расписания")
          markup.add(item1, item2, item3, item4)
          bot.send_message(message.chat.id, "Выберите команду.",
          parse_mode='html', reply_markup=markup)
        #---------------------------------------------------------------------------  
        elif message.text == 'Отключить':
          user_id = message.from_user.id
          sql = "UPDATE users SET accpet = %s WHERE id = %s"
          val = (0, user_id)
          cursor.execute(sql, val)
          user = cursor.fetchone()
          db.commit()
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          item1 = types.KeyboardButton("Расписание на сегодня")
          item2 = types.KeyboardButton("Расписание на неделю")
          item3 = types.KeyboardButton("Расписание звонков")
          item4 = types.KeyboardButton("Рассылка расписания")
          markup.add(item1, item2, item3, item4)
          bot.send_message(message.chat.id, "Выберите команду.",
          parse_mode='html', reply_markup=markup)
        #---------------------------------------------------------------------------
        elif message.text == 'Отмена':
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          item1 = types.KeyboardButton("Расписание на сегодня")
          item2 = types.KeyboardButton("Расписание на неделю")
          item3 = types.KeyboardButton("Расписание звонков")
          item4 = types.KeyboardButton("Рассылка расписания")
          markup.add(item1, item2, item3, item4)
          bot.send_message(message.chat.id, "Выберите команду.",
          parse_mode='html', reply_markup=markup)
          #print(message.chat.id)
        #---------------------------------------------------------------------------
        elif message.text == 'Расписание на сегодня':
          my_date = date.today()
          today = calendar.day_name[my_date.weekday()]
          user_id = message.from_user.id
          #print(today)
          if today == 'Monday':
            bot.send_message(message.chat.id, "Расписание на сегодня:")
            sql = "SELECT \
                  classes.Monday AS class \
                  FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
            val = (user_id, )
            cursor.execute(sql, val)
            users = cursor.fetchall()
            for user in users:
              bot.send_message(message.chat.id, user[0])
              print(user[0])
          #---------------------------------------------------------------------------
          elif today == 'Tuesday':
            bot.send_message(message.chat.id, "Расписание на сегодня:")
            sql = "SELECT \
                  classes.Tuesday AS class \
                  FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
            val = (user_id, )
            cursor.execute(sql, val)
            users = cursor.fetchall()
            for user in users:
              bot.send_message(message.chat.id, user[0])
              print(user[0])
          #---------------------------------------------------------------------------
          elif today == 'Wednesday':
            bot.send_message(message.chat.id, "Расписание на сегодня:")
            sql = "SELECT \
                  classes.Wednesday AS class \
                  FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
            val = (user_id, )
            cursor.execute(sql, val)
            users = cursor.fetchall()
            for user in users:
              bot.send_message(message.chat.id, user[0])
              print(user[0].split(', '))
          #---------------------------------------------------------------------------
          elif today == 'Thursday':
            bot.send_message(message.chat.id, "Расписание на сегодня:")
            sql = "SELECT \
                  classes.Thursday AS class \
                  FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
            val = (user_id, )
            cursor.execute(sql, val)
            users = cursor.fetchall()
            for user in users:
              bot.send_message(message.chat.id, user[0])
              print(user[0])
          #---------------------------------------------------------------------------   
          elif today == 'Friday':
            bot.send_message(message.chat.id, "Расписание на сегодня:")
            sql = "SELECT \
                  classes.Friday AS class \
                  FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
            val = (user_id, )
            cursor.execute(sql, val)
            users = cursor.fetchall()
            for user in users:
              bot.send_message(message.chat.id, user[0])
              print(user[0])
          else:
            bot.send_message(message.chat.id, "Сегодня выходной")
          db.commit()
        #---------------------------------------------------------------------------
        elif message.text == 'Расписание на неделю':
          user_id = message.from_user.id
          bot.send_message(message.chat.id, "Расписание на всю неделю:")
          sql = "SELECT \
                classes.Monday AS class \
                FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
          val = (user_id, )
          cursor.execute(sql, val)
          users = cursor.fetchall()
          for user in users:
            bot.send_message(message.chat.id, "Понедельник:\n"+user[0])
            print(user[0])
        #---------------------------------------------------------------------------
          
          sql = "SELECT \
                classes.Tuesday AS class \
                FROM users\
                INNER JOIN classes ON users.class = classes.id AND users.id = %s "
          val = (user_id, )
          cursor.execute(sql, val)
          users = cursor.fetchall()
          for user in users:
            bot.send_message(message.chat.id, "Вторник:\n"+user[0])
            print(user[0])
        #---------------------------------------------------------------------------
          
          sql = "SELECT \
                classes.Wednesday AS class \
                FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
          val = (user_id, )
          cursor.execute(sql, val)
          users = cursor.fetchall()
          for user in users:
            bot.send_message(message.chat.id, "Среда:\n"+user[0])
            print(user[0].split(', '))
        #---------------------------------------------------------------------------
          
          sql = "SELECT \
                classes.Thursday AS class \
                FROM users\
                  INNER JOIN classes ON users.class = classes.id AND users.id = %s "
          val = (user_id, )
          cursor.execute(sql, val)
          users = cursor.fetchall()
          for user in users:
            bot.send_message(message.chat.id, "Четверг:\n"+user[0])
            print(user[0])
        #---------------------------------------------------------------------------   
          
          sql = "SELECT \
                classes.Friday AS class \
                FROM users\
                INNER JOIN classes ON users.class = classes.id AND users.id = %s "
          val = (user_id, )
          cursor.execute(sql, val)
          users = cursor.fetchall()
          for user in users:
            bot.send_message(message.chat.id, "Пятница:\n"+user[0])
            print(user[0])
          db.commit()
        #--------------------------------------------------------------------------- 
        elif message.text == 'Расписание звонков':
          bot.send_message(message.chat.id, "Расписание звонков:")
          sql = "SELECT * FROM bells"
          cursor.execute(sql)
          bells = cursor.fetchall()
          nums = ['1 урок','2 урок','3 урок','4 урок','5 урок','6 урок']
          i=0
          for bell in bells:
            bot.send_message(message.chat.id, nums[i]+": "+bell[1])
            print(bell[0])
            i=i+1
          db.commit()
        #---------------------------------------------------------------------------
        elif message.text == 'Рассылка расписания': 
          user_id = message.from_user.id
          sql = "SELECT accpet FROM users WHERE id = %s"
          val = (user_id, )
          cursor.execute(sql, val)
          user = cursor.fetchone()
          print(user[0])
          if user[0]==0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Включить")
            item2 = types.KeyboardButton("Отмена")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Вы хотите включить рассылку?",
            parse_mode='html', reply_markup=markup)
          elif user[0]==1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Отключить")
            item2 = types.KeyboardButton("Отмена")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Вы хотите отключить рассылку?",
            parse_mode='html', reply_markup=markup)
          db.commit()
############################################################################################################################        
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)