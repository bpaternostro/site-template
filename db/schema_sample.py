import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        signed INTEGER,
        session VARCHAR(16)
    );'''
)

cursor.execute(
    '''CREATE TABLE lists(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        summary VARCHAR(32),
        status INTEGER,
        owner INTEGER
    );'''
)

cursor.execute(
    '''CREATE TABLE tasks(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        id_list INTEGER,
        summary VARCHAR(32),
        status INTEGER
    );'''
)

cursor.execute(
    '''CREATE TABLE status(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        summary VARCHAR(32)    
    );'''
)

connection.commit()
cursor.close()
connection.close()