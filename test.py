import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor() # cursor is a object that allows to execute queries

create_table = '''CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)'''

cursor.execute(create_table)

insert_data1 = '''INSERT INTO users(id, username, password) VALUES (3, 'mike', '1234')'''

cursor.execute(insert_data1)

user2 = (2, 'juan', '5678')
insert_data2 = '''INSERT INTO users(id, username, password) VALUES (?, ?, ?)'''
cursor.execute(insert_data2, user2)

connection.commit()

connection.close()