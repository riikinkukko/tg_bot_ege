# Импортируем библиотеку для работы с БД
import sqlite3 as sql

def add(content, answer):
    """ Функция добавления значений в базу данных """
    connect = 0
    try:
        # Соединяемся с БД
        connect = sql.connect('bot.db')
        cursor = connect.cursor()

        # Добавляем данные в нужные поля
        cursor.execute("INSERT OR IGNORE INTO `task1` (`content`) VALUES (?)", (content,))
        cursor.execute("INSERT OR IGNORE INTO `task1` (`answer`) VALUES (?)", (answer,))

        # Сохраняем изменения
        connect.commit()

    except sql.Error as Error:
        #В случае возникновения ошибок выводим их в консоль
        print('Error', Error)

    finally:
        if connect:
            connect.close()
        # Закрываем соединение с БД
        return "Time's up"

# Вставляем аргументы для функции
content, answer = 'Угол ACB равен 42°. Градусная мера дуги AB окружности, не содержащей точек D и E, равна 124°. Найдите угол DAE. Ответ дайте в градусах.', '20'

# Вызываем функцию с параметрами
add(content=content, answer=answer)