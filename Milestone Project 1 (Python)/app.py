import sys, os
import auth
import views 
import models
import database 

User = models.User
DB = database.db()

print(" Serving Nigeria, One Transaction at a time.\n Press any key to continue....... \n ==> ")
input()
print("\n Welcome to Charis Bank..\n Please Enter your UserName to proceed ")

user_id = input()

User_View = views.user_view()

user = auth.verify_users(user_id)

while user == False:

    print(" User Does not Exist....\n Press 1 to try again or Press 2 to Register as a new user or Q to QUIT. ")

    action = input()
    
    while action not in ['1', '2', 'Q']:
        print(" Press 1 to try again or Press 2 to Register as a new user or Q to QUIT. ")
        action = input()
    else:
        pass

    if action == '1':
        print("Please enter your username:    ")
        user_id = input()
        user = auth.verify_users(user_id)
    elif action == '2':
        user_id = User_View.register_user()
        user = auth.verify_users(user_id)
    else:
        sys.exit()
else:
    pass
     
         
print(" Please enter your secret password to continue \n ==> ")
pwd = input()

authenticated = auth.verify_pwd(pwd, user_id)

while not authenticated:
    print("Incorrect Password...Please Try again")
    pwd=(input(" Please Enter your secret Password:   "))
    authenticated = auth.verify_pwd(pwd, user_id)

else:
    pass



user = User(user_id, DB.query(user_id)['email'], DB.query(user_id)['password'],
        DB.query(user_id)['name'], DB.query(user_id)['contact'])

print(f" Welcome {user.get_firstname()} to Charis Bank \n ")

choice = User_View.transactions_view()

while choice == "A" or choice == "B" or choice == "C" or choice == "D":
    if choice == "A":
        choice = User_View.instant_transfer(user.username)
     
    elif choice == "B":
        choice = User_View.Mobile_Top_up(user.username)

    elif choice == "C":
        choice = User_View.check_balance(user.username)

    elif choice == "D":
        choice = User_View.withdrawal(user.username)