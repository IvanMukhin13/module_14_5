import sqlite3


def initiate_db(name_db):
    connection = sqlite3.connect(f'{name_db}.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт{i}', f'Описание{i}', f'Цена: {i * 10}'))
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL)
        ''')
    connection.commit()
    connection.close()


def get_all_products(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    list_ = cursor.fetchall()
    all_prod = []
    for i in list_:
        result = (f'Название: {i[0]} | Описание: {i[1]} | {i[2]}')
        all_prod.append(result)
    return all_prod


def add_user(username, email, age):
    '''
    Функция принимает: имя пользователя, почту и возраст. Данная функция должна
    добавлять в таблицу Users вашей БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000.
    Для добавления записей в таблице используйте SQL запрос.
    :param username: str
    :param email: str
    :param age: int
    :return:
    '''
    connection = sqlite3.connect('Product_db.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    '''
    Функция принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users,
    в противном случае False. Для получения записей используйте SQL запрос.
    :param username: str
    :return: True or False
    '''
    connection = sqlite3.connect('Product_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM Users')
    list_usernames = []
    for user in cursor.fetchall():
        for pr in user:
            list_usernames.append(pr)
    if username in list_usernames:
        return True
    else:
        return False






