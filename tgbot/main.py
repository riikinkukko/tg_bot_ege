import telebot
from telebot import types
import sqlite3 as sql
from bot_token import BOT_TOKEN
import random

bot = telebot.TeleBot(BOT_TOKEN)

#Стартовая клавиатура
kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton(text='Решать задания первой части')
btn2 = types.KeyboardButton(text='Решить случайный вариант')
kb.add(btn1, btn2)

#Фукнция стартовой загрузки и возвращения в стартовое меню
@bot.message_handler(func=lambda message: message.text == 'Назад')
@bot.message_handler(commands=['start', 'back'])
def start(message):
    connect = sql.connect('bot.db') #Подлючение к БД
    cursor = connect.cursor()
    people_id = message.chat.id
    cursor.execute("SELECT `user_id` FROM `users` WHERE `user_id` = ?", (people_id,))
    data = cursor.fetchone()
    zero = 0
    #В случае, если пользователь впервые посещает бота, добавляем его в БД
    if data is None:
        cursor.execute("INSERT INTO `users` ('user_id', 'task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7', 'task8', 'task9', 'task10', 'task11', 'task12') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (people_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        connect.commit()
        bot.send_message(message.chat.id, 'Привет! Это телеграм-бот для подготовки к ЕГЭ по математике',
                         reply_markup=kb)
    #Отправляем сообщение и стартовое меню
    bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Решить случайный вариант')
def variant(message):
    id = message.chat.id
    l = [random.randint(1, 5) for i in range(12)] #Генерация рандомных 12 чисел
    connect = sql.connect('bot.db') #Подключение к БД
    cursor = connect.cursor()

    #Выбор случайного задания для конкретного пункта задачи ЕГЭ и отправка его пользователю

    #1
    cursor.execute('SELECT `content` FROM `task1` where `id` = ?', (l[0],))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/1/image{l[0]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task1` where `id` = ?', (l[0],))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1) if content1[0] != '' else print('No')
    bot.send_photo(message.chat.id, image1)
    #2
    cursor.execute('SELECT `content` FROM `task2` where `id` = ?', (l[1],))
    content2 = cursor.fetchone()

    image1 = open(f'images/2/image{l[1]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task2` where `id` = ?', (l[1],))
    answer2 = cursor.fetchone()

    bot.send_message(message.chat.id, content2[0]) if content2[0] != '' else print('No')
    bot.send_photo(message.chat.id, image1)
    #3
    cursor.execute('SELECT `content` FROM `task3` where `id` = ?', (l[2],))
    content3 = cursor.fetchone()

    image1 = open(f'images/3/image{l[2]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task3` where `id` = ?', (l[2],))
    answer3 = cursor.fetchone()

    bot.send_message(message.chat.id, content3[0]) if content3[0] != '' else print('No')
    bot.send_photo(message.chat.id, image1)
    #4
    cursor.execute('SELECT `content` FROM `task4` where `id` = ?', (l[3],))
    content4 = cursor.fetchone()

    bot.send_message(message.chat.id, content4[0]) if content4[0] != '' else print('No')
    image1 = open(f'images/4/image{l[3]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task4` where `id` = ?', (l[3],))
    answer4 = cursor.fetchone()
    bot.send_photo(message.chat.id, image1)
    #5
    cursor.execute('SELECT `content` FROM `task5` where `id` = ?', (l[4],))
    content5 = cursor.fetchone()

    image1 = open(f'images/5/image{l[4]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task5` where `id` = ?', (l[4],))
    answer5 = cursor.fetchone()

    bot.send_message(message.chat.id, content5[0]) if content5[0] != '' else print('No')
    bot.send_photo(message.chat.id, image1)
    #6

    cursor.execute('SELECT `content` FROM `task6` where `id` = ?', (l[5],))
    content6 = cursor.fetchone()

    image1 = open(f'images/6/image{l[5]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task6` where `id` = ?', (l[5],))
    answer6 = cursor.fetchone()

    bot.send_message(id, content6[0]) if content6[0] != '' else print('No')
    bot.send_photo(id, image1)
    #7
    cursor.execute('SELECT `content` FROM `task7` where `id` = ?', (l[6],))
    content7 = cursor.fetchone()

    image1 = open(f'images/7/image{l[6]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task7` where `id` = ?', (l[6],))
    answer7 = cursor.fetchone()

    bot.send_message(id, content7[0]) if content7[0] != '' else print('No')
    bot.send_photo(id, image1)
    #8
    cursor.execute('SELECT `content` FROM `task8` where `id` = ?', (l[7],))
    content8 = cursor.fetchone()

    image1 = open(f'images/8/image{l[7]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task8` where `id` = ?', (l[7],))
    answer8 = cursor.fetchone()

    bot.send_message(id, content8[0]) if content8[0] != '' else print('No')
    bot.send_photo(id, image1)
    #9
    cursor.execute('SELECT `content` FROM `task9` where `id` = ?', (l[8],))
    content9 = cursor.fetchone()

    image1 = open(f'images/9/image{l[8]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task9` where `id` = ?', (l[8],))
    answer9 = cursor.fetchone()

    bot.send_message(id, content9[0]) if content9[0] != '' else print('No')
    bot.send_photo(id, image1)
    #10
    cursor.execute('SELECT `content` FROM `task10` where `id` = ?', (l[9],))
    content10 = cursor.fetchone()

    image1 = open(f'images/10/image{l[9]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task10` where `id` = ?', (l[9],))
    answer10 = cursor.fetchone()

    bot.send_message(id, content10[0]) if content10[0] != '' else print('No')
    bot.send_photo(id, image1)
    #11
    cursor.execute('SELECT `content` FROM `task11` where `id` = ?', (l[10],))
    content11 = cursor.fetchone()

    image11 = open(f'images/11/image{l[10]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task11` where `id` = ?', (l[10],))
    answer11 = cursor.fetchone()

    bot.send_message(id, content11[0]) if content11[0] != '' else print('No')
    bot.send_photo(id, image11)
    #12
    cursor.execute('SELECT `content` FROM `task11` where `id` = ?', (l[11],))
    content12 = cursor.fetchone()

    image12 = open(f'images/12/image{l[11]}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task12` where `id` = ?', (l[11],))
    answer12 = cursor.fetchone()

    bot.send_message(id, content12[0]) if content12[0] != '' else print('No')
    bot.send_photo(id, image12)
    cursor.close()

    #Список ответов, передаваемых в функцию проверки ответов
    answers = [
            answer1, answer2[0], answer3[0],
            answer4[0], answer5[0], answer6[0],
            answer7[0], answer8[0], answer9[0],
            answer10[0], answer11[0], answer12[0]
        ]

    last_message = bot.send_message(message.chat.id, 'Напиши ответы одним сообщением через запятую')

    bot.register_next_step_handler(last_message, answer_check, answers)

#Функция проверки ответов варианта
def answer_check(message, answers, count=0):
    if message.text == 'Назад' or message.text == '/back':
        m = bot.send_message(message.chat.id, 'Возвращаю обратно')
        bot.register_next_step_handler(m, start)
    else:
        a = list(message.text.split(','))
        for i in range(len(a)):
            if a[i] == str(answers[i]):
                print(a[i], answers[i])
                count += 1
            print(a[i], answers[i])
        connect = sql.connect('bot.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE `users` SET (`pred_result`) = ? WHERE user_id = ?", (count, message.chat.id))
        connect.commit()
        m = bot.send_message(message.chat.id, f'Набрано баллов {count} из 12')
        cursor.close()

@bot.message_handler(func=lambda message: message.text == 'Решать задания первой части')
def tasks(message):
    #Меню выбора конкретного задания
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Задание 1')
    btn2 = types.KeyboardButton(text='Задание 2')
    btn3 = types.KeyboardButton(text='Задание 3')
    btn4 = types.KeyboardButton(text='Задание 4')
    btn5 = types.KeyboardButton(text='Задание 5')
    btn6 = types.KeyboardButton(text='Задание 6')
    btn7 = types.KeyboardButton(text='Задание 7')
    btn8 = types.KeyboardButton(text='Задание 8')
    btn9 = types.KeyboardButton(text='Задание 9')
    btn10 = types.KeyboardButton(text='Задание 10')
    btn11 = types.KeyboardButton(text='Задание 11')
    btn12 = types.KeyboardButton(text='Задание 12')
    btn13 = types.KeyboardButton(text='Назад')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    bot.send_message(message.chat.id, 'Выберите задание', reply_markup=keyboard)


#Далее - функции обработки и отправки конкретного задания (task1-12)
@bot.message_handler(func=lambda message: message.text == 'Задание 1')
def task1(message):

    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task1` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task1` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/1/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task1` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 1
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)

@bot.message_handler(func=lambda message: message.text == 'Задание 2')
def task2(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task2` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task2` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/2/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task2` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 2
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)

@bot.message_handler(func=lambda message: message.text == 'Задание 3')
def task3(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task3` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task3` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/3/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task3` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 3
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 4')
def task4(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task4` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task4` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/4/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task4` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 4
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 5')
def task5(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task5` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task5` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/5/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task5` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 5
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 6')
def task6(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task6` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task6` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/6/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task6` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 6
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 7')
def task7(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task7` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task7` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/7/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task7` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 7
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 8')
def task8(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task8` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task8` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/8/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task8` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 8
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 9')
def task9(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task9` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task9` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/9/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task9` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    a = list(message.text.split(','))

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 9
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 10')
def task10(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task10` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0] + 1

    cursor.execute('SELECT `content` FROM `task10` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/10/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task10` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 10
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 11')
def task11(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task11` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0]

    cursor.execute('SELECT `content` FROM `task11` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/11/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task11` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 11
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)


@bot.message_handler(func=lambda message: message.text == 'Задание 12')
def task12(message):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()

    cursor.execute('SELECT `task12` FROM `users` where `user_id` = ?', (message.chat.id,))
    number_of_task = cursor.fetchone()[0]

    cursor.execute('SELECT `content` FROM `task12` where `id` = ?', (number_of_task,))
    content1 = cursor.fetchone()[0]

    image1 = open(f'images/12/image{number_of_task}.jpg', 'rb')

    cursor.execute('SELECT `answer` FROM `task12` where `id` = ?', (number_of_task,))
    answer1 = cursor.fetchone()[0]

    bot.send_message(message.chat.id, content1)
    m = bot.send_photo(message.chat.id, image1)

    task = 12
    bot.register_next_step_handler(m, check_task, number_of_task, answer1, task)

#Функция проверки ответа на конкретное задание
def check_task(message, number_of_task, answer1, task):
    connect = sql.connect('bot.db')
    cursor = connect.cursor()
    a = message.text

    if a == answer1:
        bot.send_message(message.chat.id, 'Правильно')
        cursor.execute(f"UPDATE `users` SET (`task{task}`) = ? WHERE user_id = ?", (number_of_task+1, message.chat.id))
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Неправильно')

#Бесконечная работа бота
bot.infinity_polling()