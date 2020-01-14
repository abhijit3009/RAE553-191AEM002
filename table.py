import sqlite3

connection = sqlite3.connect('data.db')#creating data.db database 
cursor = connection.cursor()# creatting a Cursor object 

#creating a TABLE for users
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
#creating a TABLE for items
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)
#inserting data for test item
cursor.execute("INSERT INTO items VALUES ('test item', '123456789')")

connection.commit() 
connection.close()
