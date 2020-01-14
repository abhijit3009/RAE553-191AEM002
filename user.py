import sqlite3 # importing sqlite3
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('username', type=str,required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str,required=True, help='This field cannot be left blank')

    #defining post to create users
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message":"A user with this username is already exists"}, 400
        connection = sqlite3.connect('data.db')
        cursor =   connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"message": "User Create Successfully!!!"}, 201

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #verify the username exists in database
    @classmethod
    def find_by_username(cls, username):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE username=?" #select every row in the database 
        result = cursor.execute(query, (username,)) 
        row = result.fetchone() #selects the first row 
        if row:
            user = cls(*row)
        else:
            user = None # 
        
        connection.close()
        return user
    #verify the id which is in database
    @classmethod
    def find_by_id(cls, id):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE id=?" #select every row in the database 
        result = cursor.execute(query, (id,)) 
        row = result.fetchone() #selects the first row 
        if row:
            
            user = cls(*row)
        else:
            user = None 
        
        connection.close()
        return user
