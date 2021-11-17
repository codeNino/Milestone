import sqlite3, sys, traceback
from datetime import datetime

# HOW TO CREATE A DATABASE AND DATABASE CONNECTION IN SQLITE

# try:
#     sqliteConnection = sqlite3.connect('Milestone_db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")

#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")



# CREATE TABLES IN SQLITE DATABASE

# try:
#     connector = sqlite3.connect('Milestone_db')
#     cursor = connector.cursor()
#     print("Successfully created database connection")
    
#     query = '''DROP TABLE IF EXISTS `Milestone_Users`;'''

#     cursor.execute(query)
#     connector.commit()
#     query = ''' CREATE TABLE `Milestone_Users` (
#                                 id INTEGER PRIMARY KEY,
#                                 name TEXT NOT NULL, username TEXT NOT NULL UNIQUE,
#                                 email TEXT NOT NULL UNIQUE, contact TEXT NOT NULL,
#                                 joining_date TEXT, password TEXT NOT NULL,
#                                 account_balance INTEGER NULL );'''
#     cursor.execute(query)
#     connector.commit()
#     print("SQLite Users table created")

#     query = '''DROP TABLE IF EXISTS `Milestone_Admin`;'''  
#     cursor.execute(query)
#     connector.commit()

#     query = '''CREATE TABLE `Milestone_Admin` (
#                                 id INTEGER PRIMARY KEY,
#                                 adminID TEXT NOT NULL UNIQUE,
#                                 email TEXT NOT NULL UNIQUE,
#                                 last_login TEXT, password TEXT NOT NULL
#                                 );'''
#     cursor.execute(query)
#     connector.commit()
    
#     print("SQLite Admin table created")
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if connector:
#         connector.close()
#         print("sqlite connection is closed")


# HOW TO INSERT INTO AN SQLITE TABLE 


# try:
#     conn = sqlite3.connect('Milestone_db')
#     cursor = conn.cursor()
#     print("Successfully Connected to SQLite")


#     query = f"""INSERT INTO `Milestone_Users` (name, username, email, password, contact, joining_date)  VALUES  ('Jane Doe',
#                           'jane_d', 'janedoe@python.com', 'jane_doe56', '0987654321', '{str(datetime.now())}');"""

#     cursor.execute(query)
#     # count = cursor.execute(query)
#     conn.commit()
#     print("Record inserted successfully into table ", cursor.rowcount)
#     cursor.close()

# except sqlite3.Error as error:
#     print("Failed to insert data into sqlite table")
#     print("Exception class is: ", error.__class__)
#     print("Exception is", error.args)
#     print('Printing detailed SQLite exception traceback: ')
#     exc_type, exc_value, exc_tb = sys.exc_info()
#     print(traceback.format_exception(exc_type, exc_value, exc_tb))
# finally:
#     if (conn):
#         conn.close()
#         print("The SQLite connection is closed")

# # HOT TO READ DATA FROM SQLITE DB

# def readSqliteTable():
#     try:
#         Connection = sqlite3.connect('Milestone_db', timeout=20)
#         cursor = Connection.cursor()
#         print("Connected to SQLite")

#         query = """SELECT * from Milestone_Users"""
#         cursor.execute(query)
#         totalRows = cursor.fetchall()
#         for row in totalRows:
#             print(row)
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read data from sqlite table", error)
#     finally:
#         if Connection:
#             Connection.close()
#             print("The Sqlite connection is closed")

# readSqliteTable()


# HOW TO UPDATE A SQLITE DB

# try:
#     Connection = sqlite3.connect('Milestone_db')
#     cursor = Connection.cursor()
#     print("Connected to SQLite")

#     # query = """Update Milestone_Users set account_balance = 10000 where name = 'John Doe' """
#     # cursor.execute(query)

#     sql_delete_query = """DELETE from Milestone_Users where id = 1"""
#     cursor.execute(sql_delete_query)

#     Connection.commit()
#     # cursor.close()

# except sqlite3.Error as error:
#     print("Error while working with SQLite", error)
# finally:
#     if Connection:
#         cursor.execute("""Select * from Milestone_Users""")
#         for row in cursor.fetchall():
#             print(row)
#         Connection.close()
#         print("sqlite connection is closed")


import sqlite3


conn = sqlite3.connect('Milestone_db')
cursor = conn.cursor()

# query = """INSERT INTO `Milestone_Admin` (adminID, email, password)  
#             VALUES  ('nino','nino@python.com', 'nino7');"""
# cursor.execute(query)

query = """select * from `Milestone_Admin`;"""
cursor.execute(query)
print(cursor.fetchall())
conn.close()