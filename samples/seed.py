import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password
    ) VALUES (
        'Gordon',
        'Ramsay'
    );"""
)

cursor.execute(
    """INSERT INTO users(
        username,
        password
    ) VALUES (
        'Ironman',
        'Tony'
    );"""
)

connection.commit()
cursor.close()
connection.close()