import database, models, auth
import sys, time, json, os, pandas as pd

Admin = models.Admin

user_db_path = os.path.abspath(r"C:\Users\lordn\Milestone Projects\Milestone Project 1 (Python)\userDB.txt")

admin_db_path = os.path.abspath(r"C:\Users\lordn\Milestone Projects\Milestone Project 1 (Python)\adminDB.txt")

def check_admin(admin_id):
    with open(admin_db_path, 'r') as f:
         opened_file = f.readlines() 
         if opened_file == "":
            f.close()
            return None
         else:
            data = {} 
            for line in opened_file:
               data.update(dict(json.loads(line)))
               f.close()
            return data.get(admin_id, None)


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
            self.__adminID = admin_id
            self.__admin = Admin(self.__adminID, check_admin(self.__adminID)["password"],
                        check_admin(self.__adminID)["email"])
            return self.home_page()


    def home_page(self):
        print(f"Hello {self.__adminID}, welcome to the admin panel.")
        print("To view Database records Enter '1' or Enter 2 to Quit..")
        action = input("==>  ")
        while action != "1" and action != "2":
            print(f"Hello {self.__adminID}, welcome to the admin panel.")
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
            
            data = {}
            with open(user_db_path,'r') as db:
                opened_file = db.readlines()
                for line in opened_file:
                    data.update(dict(json.loads(line)))
            db.close()
            print("Database loading....")

            [x["email"] for x in data.values()]
            names = [x["name"] for x in data.values()]
            emails = [x["email"] for x in data.values()]
            contacts = [x["contact"] for x in data.values()]
            pwds = [x["password"] for x in data.values()]
            acc_bal = [x["account balance"] for x in data.values()]
            usernames = [x for x in data.keys()]
            data_dict = {"UserID": usernames, "Name": names,
                        "Email": emails, "Contact": contacts,
                            "Password": pwds, "Balance": acc_bal}
            db_table = pd.DataFrame(data=data_dict)
            print(db_table)

                
        def __view_adminDB():
            
            data = {}
            with open(admin_db_path,'r') as db:
                opened_file = db.readlines()
                for line in opened_file:
                    data.update(dict(json.loads(line)))
            db.close()
            print("Database loading....")

            emails = [x["email"] for x in data.values()]
            pwds = [x["password"] for x in data.values()]
            id = [x for x in data.keys()]
            data_dict = {"adminID": id,
                        "Email": emails,
                            "Password": pwds}
            db_table = pd.DataFrame(data=data_dict)
            print(db_table)

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
