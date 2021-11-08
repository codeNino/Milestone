import sys
import auth
import views 
import models
import database 

User = models.User
db = database.db

print(" Serving Nigeria, One Transaction at a time.\n Press any key to continue....... \n ==> ")
input()
print("\n Welcome to Charis Bank..\n Please Enter your UserName to proceed ")

user_id = input()

User_View = views.user_view()

user = auth.verify_users(user_id)

while user == False:

    print(" User Does not Exist....\n Press 1 to try again or Press 2 to Register as a new user")

    action = input()

    if action == '1':
        print("Please enter your username:    ")
        name = input()
        user = auth.verify_users(name)

    else:
        user_id = User_View.register_user()
        user = auth.verify_users(user_id)

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



user = User(user_id, db[user_id]['email'], db[user_id]['password'],
        db[user_id]['name'], db[user_id]['contact'])

print(f" Welcome {user.get_firstname()} to Charis Bank \n ")


choice = User_View.transactions_view()

while choice == "A" or choice == "B" or choice == "C" or choice == "D":
    if choice == "A":
        choice = User_View.instant_transfer_view(user.username)
     
    elif choice == "B":
        # choice = Mobile_Top_up(user.user_id)
        sys.exit()

    elif choice == "C":
        # choice = check_balance(user.user_id)
        sys.exit()

    elif choice == "D":
        # choice = withdrawal(user.user_id)
        sys.exit()


else:
    sys.exit()