import sqlite3

def add_user(username, password):

    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT username FROM users WHERE username='{username}';""".format(username = username))
    validation=False
    if cursor.fetchone() == None:
        cursor.execute(
        """INSERT INTO users(
            username,
            password
        ) VALUES (
            '{username}',
            '{password}'
        );""".format(username = username,password = password))
        
        validation=True

    connection.commit()
    cursor.close()
    connection.close()

    return validation

def get_user(username, password):

    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT count(1) as cant FROM users WHERE username='{username}' and password='{password}' GROUP BY username;""".format(username = username,password = password))
    validation=False
    if cursor.fetchone() != None:
        validation=True

    connection.commit()
    cursor.close()
    connection.close()

    return validation


def show_color(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT favorite_color FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    color=cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message = '{username}\'s favorite color is {color}.'.format(username=username, color=color)
    return message


def check_pw(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" Select password from users where username='{username}';""".format(username= username))
    passsword = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return passsword


def signup(username,passsword,favorite_color):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    #valid if the user if exist
    cursor.execute(""" Select password from users where username='{username}';""".format(username = username))

    exist = cursor.fetchone()[0]

    if exist is None:
        cursor.execute(""" INSERT INTO users(username,password,favorite_color) VALUES('{username}','{password}','{favorite_color}');""").format(username = username, passsword = passsword, favorite_color=favorite_color)
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return ('User already existed!!!!!!')
    
    return "You have successfully signed up!!" 

def check_users():
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" Select username from users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person=db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    return users