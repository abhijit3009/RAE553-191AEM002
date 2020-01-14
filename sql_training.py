import sqlite3
import random
import string

connection = sqlite3.connect('data.db')#creating data.db database 
cursor = connection.cursor()# creatting a Cursor object 

#creating a TABLE
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


user = (1, 'Abhijit', 'Abhi1234')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit() 

# defining for generating username and password 
def dynamic_user_generate(num):
    name = ''.join([random.choice(string.ascii_uppercase) for n in range(6)]) 
    pas = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(10)])      
    cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (num, name, pas)) #
    connection.commit() 

for i in range(2,6):# calling to generate random username and password
    dynamic_user_generate(i)

for row in cursor.execute('SELECT * FROM users ORDER BY id'):
    print(row)


connection.close()
