import sqlite3, sys, traceback
from datetime import datetime
import models

User = models.User

conn = sqlite3.connect('Milestone_db')

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS `Milestone_Users` (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL, username TEXT NOT NULL UNIQUE,
                                email TEXT NOT NULL UNIQUE, contact TEXT NOT NULL,
                                 joining_date TEXT, password TEXT NOT NULL, account_balance INTEGER DEFAULT 0 );''')

conn.commit()
cursor.close()
conn.close()


class db():

    def add(self, user: User):
        conn = sqlite3.connect('Milestone_db')
        cursor = conn.cursor()

        try:
            query = f"""INSERT INTO `Milestone_Users` (name, username, email, password, contact, joining_date)  
            VALUES  ('{user.fullname}',
                    '{user.username}', '{user.email}', '{user.get_pwd()}', '{user.contact}', 
                    '{str(datetime.now())}');"""

            cursor.execute(query)
            conn.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table")
            print("Exception class is: ", error.__class__)
            print("Exception is", error.args)
            print('Printing detailed SQLite exception traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        finally:
            if conn:
                conn.close()


    def read(self, filter_by: dict):
        conn = sqlite3.connect('Milestone_db')
        cursor = conn.cursor()

        try:
            key, value = list(filter_by.keys())[0], list(filter_by.values())[0]
            query = f"""SELECT * from Milestone_Users where `{key}` = '{value}' """
            data = cursor.execute(query)
            result = cursor.fetchone()
            assert result is not None
            row = tuple(result)
            columns  = tuple([x[0] for x in data.description])
            data = {x:y for x,y in zip(columns,row)}
            cursor.close()
            return data

        except AssertionError:
            return None

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if conn:
                conn.close()

    def update(self, update: dict, by: dict):
        conn = sqlite3.connect('Milestone_db')
        cursor = conn.cursor()

        try:
            by_key, by_value = list(by.keys())[0], list(by.values())[0]

            for x,y in update.items():
                query = f"""Update Milestone_Users set `{x}` = '{y}' where `{by_key}` = '{by_value}' """
                cursor.execute(query)
                conn.commit()
        except sqlite3.Error as error:
          print("Error while working with SQLite", error)
        finally:
            if conn:
                # cursor.execute("""Select * from Milestone_Users""")
                # for row in cursor.fetchall():
                #     print(row)
                conn.close()

    def delete(self, by: dict):
        conn = sqlite3.connect('Milestone_db')
        cursor = conn.cursor()

        by_key, by_value = list(by.keys())[0], list(by.values())[0]
        try:
            query = f"""DELETE from Milestone_Users where `{by_key}` = '{by_value}' """
            cursor.execute(query)
            conn.commit()
        except sqlite3.Error as error:
          print("Error while working with SQLite", error)
        finally:
            if conn:
                # cursor.execute("""Select * from Milestone_Users""")
                # for row in cursor.fetchall():
                #     print(row)
                conn.close()