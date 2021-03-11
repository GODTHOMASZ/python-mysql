@bot.message_handler(commands=['today'])
def send_today_scheudle(message):
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
#----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['week'])
def send_week_scheudle(message):
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
#------------------------------------------------------------------------------------------------------------------------------------------------------      
@bot.message_handler(commands=['bell'])
def send_bell_scheudle(message):
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
#------------------------------------------------------------------------------------------------------------------------------------------------------      
@bot.message_handler(commands=['mailing'])
def send_mailing_scheudle(message):
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