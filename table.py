import sqlite3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()


create_table = ('''CREATE TABLE IF NOT EXISTS users (id INTEGER,name text NOT NULL,password text NOT NULL)''')
cursor.execute(create_table)

users = [
(1, 'abhi', '8456'),
(2, 'may', '2305'),
(3, 'dec', '2303')
]

insert_query = ("INSERT INTO users VALUES (?, ?, ?)")

for i in users:
    cursor.execute(insert_query, (i))
connection.commit()

connection.close()

print(users)
