import sys
import mysql_db_connection as engine

DB = engine.db()

def verify_users(user_id):

    if DB.read({"username":user_id}) != None:
        return True
    else:
        return False


def transaction_auth(pwd, user_id):

    password_lim = 3
    while pwd != DB.read({"username":user_id})["password"]:
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

    if pwd != DB.read({"username":user_id})["password"]:
        return False
    else:
        return True

def validate_domain_name(domain_name):
    import re
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    compiled_regex = re.compile(regex)

    if (domain_name==None):
        return False
    
    if (re.search(compiled_regex, domain_name)):
        return True
    else:
        return False