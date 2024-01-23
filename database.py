import sqlite3

def connect_db():
    return sqlite3.connect('password_manager.db') 
    #this is a function call to 'connect' from the sqlite3 library, it creates and returns a connection object to to a sqlite database named 
    #'password_manager.db', if a databse by this name doesnt exist, it creates a new one. 


