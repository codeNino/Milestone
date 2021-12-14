import MySQLdb as sql
from datetime import datetime
import models

User = models.User

#create connection with database server
connection = sql.connect(user='root',host='127.0.0.1',port=3306,password='Oluwanino7')

#create cursor object to perform operations on server
cursor = connection.cursor()

#create database and use
cursor.execute("CREATE DATABASE IF NOT EXISTS Milestone_Project")
cursor.execute("USE Milestone_Project")

#create table if not already existing

query =  """CREATE TABLE IF NOT EXISTS `Milestone_Users` (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL, username varchar(10) NOT NULL UNIQUE,
        email varchar(30) NOT NULL UNIQUE, contact TEXT NOT NULL,
        joining_date TEXT, password TEXT NOT NULL, account_balance INTEGER DEFAULT 0 );"""

cursor.execute(query)
connection.commit()
connection.close()


class db():

    def add(self, user: User):
        conn = sql.connect(user='root',host='127.0.0.1',port=3306,password='Oluwanino7',database='Milestone_Project')
        cursor = conn.cursor()

        try:
            query = f"""INSERT INTO `Milestone_Users` (name, username, email, password, contact, joining_date)  
            VALUES  ('{user.fullname}',
                    '{user.username}', '{user.email}', '{user.get_pwd()}', '{user.contact}', 
                    '{str(datetime.now())}');"""

            cursor.execute(query)
            conn.commit()
            cursor.close()

        except sql.Error as error:
            print("Failed to insert data into sqlite table")
            print("Exception class is: ", error.__class__)
            print("Exception is", error.args)
            print('Printing detailed MySQL exception traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        finally:
            if conn:
                conn.close()


    def read(self, filter_by: dict):
        conn = sql.connect(user='root',host='127.0.0.1',port=3306,password='Oluwanino7',database='Milestone_Project')
        cursor = conn.cursor()

        try:
            key, value = list(filter_by.keys())[0], list(filter_by.values())[0]
            query = f"""SELECT * from Milestone_Users where `{key}` = '{value}' """
            cursor.execute(query)
            all_fields = cursor.description
            result = cursor.fetchone()
            assert result is not None
            row = tuple(result)
            columns = tuple([fields[0] for fields in all_fields])
            data = {x:y for x,y in zip(columns,row)}
            cursor.close()
            return data

        except AssertionError:
            return None

        except sql.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if conn:
                conn.close()

    def update(self, update: dict, by: dict):
        conn = sql.connect(user='root',host='127.0.0.1',port=3306,password='Oluwanino7',database='Milestone_Project')
        cursor = conn.cursor()

        try:
            by_key, by_value = list(by.keys())[0], list(by.values())[0]

            for x,y in update.items():
                query = f"""Update Milestone_Users set `{x}` = '{y}' where `{by_key}` = '{by_value}' """
                cursor.execute(query)
                conn.commit()
        except sql.Error as error:
          print("Error while working with SQLite", error)
        finally:
            if conn:
                conn.close()

    def delete(self, by: dict):
        conn = sql.connect(user='root',host='127.0.0.1',port=3306,password='Oluwanino7',database='Milestone_Project')
        cursor = conn.cursor()

        by_key, by_value = list(by.keys())[0], list(by.values())[0]
        try:
            query = f"""DELETE from Milestone_Users where `{by_key}` = '{by_value}' """
            cursor.execute(query)
            conn.commit()
        except sql.Error as error:
          print("Error while working with SQLite", error)
        finally:
            if conn:
                conn.close()