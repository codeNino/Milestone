import models
import sys, pandas as pd
import sqlite3, sys, traceback
from datetime import datetime

User = models.User

Admin = models.Admin

conn = sqlite3.connect('Milestone_db')
cursor = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS `Milestone_Admin` (
                                id INTEGER PRIMARY KEY,
                                adminID TEXT NOT NULL UNIQUE,
                                email TEXT NOT NULL UNIQUE,
                                last_login TEXT NULL, password TEXT NOT NULL
                                );'''
cursor.execute(query)
conn.commit()
cursor.close()


def check_admin(admin_id): 
    conn = sqlite3.connect('Milestone_db')
    cursor = conn.cursor()
    try:
        query = f"""SELECT * from Milestone_Admin where `adminID` = '{admin_id}' """
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
    finally:
        if conn:
            conn.close()


class Admin_view():

    def login_page(self):
        admin_id = input(" Admin Username ==>  ")
        pwd = input(" Admin Password ==>  ")

        while check_admin(admin_id) == None or pwd != check_admin(admin_id)["password"]:
            print("Invalid Credetials...\n")
            action = input("Enter '1' to try again or 'Q' to quit...")
            while action != "1" and action != "Q":
                action = input("Enter '1' to try again or 'Q' to quit...")
            else:
                pass
            if action == "1":
                admin_id = input(" Admin Username ==>  ")
                pwd = input(" Admin Password ==>  ")
                if check_admin(admin_id) != None and pwd == check_admin(admin_id)["password"]:
                    break
            else:
                sys.exit()
        else:
            admin_data = check_admin(admin_id)
            self.__admin = Admin(admin_id, admin_data["password"],
                        admin_data["email"])
            return self.home_page()


    def home_page(self):
        print(f"Hello {self.__admin.__adminID}, welcome to the admin panel.")
        print("To view Database records Enter '1' or Enter 2 to Quit..")
        action = input("==>  ")
        while action != "1" and action != "2":
            print(f"Hello {self.__admin.__adminID}, welcome to the admin panel.")
            print("To view Database records Enter '1' or Enter 2 to Quit..")
            action = input("==>  ")
        else:
            pass
        if action == '2':
            sys.exit()
        else:
            return self.database_view()

    def database_view(self):

        def __view_userDB():
            try:
                conn = sqlite3.connect('Milestone_db')
                cursor = conn.cursor()
                query = """SELECT * from Milestone_Users"""
                data = cursor.execute(query)
                results = cursor.fetchall()
                assert results is not None
                columns  = tuple([x[0] for x in data.description])

                ids = [x[0] for x in results]
                names = [x[1] for x in data.values()]
                usernames = [x[2] for x in data.values()]
                emails = [x[3] for x in data.values()]
                contacts = [x[4] for x in data.keys()]
                j_dates =  [x[5] for x in data.keys()]
                pwd =  [x[6] for x in data.keys()]
                acc_bal =  [x[7] for x in data.keys()]

                values = tuple(ids, names, usernames, emails, contacts, j_dates, pwd, acc_bal)

                data_dict = {x:y for x,y in zip(columns, values)}
                db_table = pd.DataFrame(data=data_dict)
                print(db_table)
            except AssertionError:
                print(" Database Empty.....")
            finally:
                conn.close()

                
        def __view_adminDB():
            try:
                conn = sqlite3.connect('Milestone_db')
                cursor = conn.cursor()
                query = """SELECT * from Milestone_Admin"""
                data = cursor.execute(query)
                results = cursor.fetchall()
                assert results is not None
                columns  = tuple([x[0] for x in data.description])

                ids = [x[0] for x in results]
                adminIDs = [x[1] for x in results]
                emails = [x[2] for x in results]
                last_login =  [x[3] for x in results]
                pwds =  [x[4] for x in results]

                values = tuple(ids, adminIDs, emails, last_login, pwds)

                data_dict = {x:y for x,y in zip(columns, values)}
                db_table = pd.DataFrame(data=data_dict)
                print(db_table)
            except AssertionError:
                print(" Database Empty.....")
            finally:
                conn.close()
            

        action = input("Enter '1' to view user records or '2' to view admin records:    ")

        while action != "1" and action != "2":
            action = input("Enter '1' to view user records or '2' to view admin records:   ")
        else:
            pass
        if action == "1":
            return __view_userDB()
        else:
            return __view_adminDB()

        print("Enter 1 to Quit or 2 to return to the home page")
        action = input(" ==>  ")

        if action == "1":
            sys.exit()
        else:
            return self.home_page()
