import sys
import database

DB = database.db()

def verify_users(user_id):

    if DB.read(user_id) != None:
        return True
    else:
        return False


def transaction_auth(pwd, user_id):

    password_lim = 3
    while pwd != DB.read(user_id)["password"]:
        print(f"Password Incorrect...\n Please Try again\n you have {password_lim} attempts left \n")
        print("Press 1 to Try Again or 2 to Quit")
        action = input()
        if action == "2":
            sys.exit()

        else:
            password_lim -= 1
            pwd = input(" Please Enter your secret Password:    ")
            if password_lim == 0:
                print("Service suspended!!")
                sys.exit()

    else:
        print("Transaction Authenticated....")


def verify_pwd(pwd, user_id):

    if pwd != DB.read(user_id)['password']:
        return False
    else:
        return True