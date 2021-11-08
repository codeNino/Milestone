import database
import models
import auth

import sys

db = database.db

User = models.User

class user_view():

    def register_user(self):

        print(" Please Fill the form Below to Register as New User\n")
        username = input(" Please Enter UserName ==>    ")
        name = input(" Please Enter your fullname ==>   ")
        passwd = input(" Please Enter your secret password ")

        while any(map(str.isdigit, passwd)) is False or any(map(str.isupper, passwd)) is False or len(passwd) < 9:

            if any(map(str.isdigit, passwd)) is False:
                print(" Password must contain digits!! \n ")
                print(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                passwd = input(" Password:    ")
            elif any(map(str.isupper, passwd)) is False: 
                print(" Password must contain upper case characters !! \n ")
                print(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                passwd = input(" Password:  ")
            elif len(passwd) < 9:
                print(" Password must be at least 9 characters long !! \n ")
                print(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                passwd = input(" Password:   ")

        else:
            pass

        confirmed_password =input("confirm password")
        while confirmed_password != passwd:
            print(' Password Not Matching ')
            confirmed_password = input(' confirm password')
        else:
            pass
        email = input(" Please Enter your Email Address:   ")
        contact = input(" Please Enter your Phone Number:   ")

        user = User(username, email, passwd, name, contact)

        db.update({user.username: {"name": user.fullname, "email": user.email, 
         "contact": user.contact, "password": user.get_pwd(), 
         'account balance': 0}})

        print("You have successfully registered!!")

        user.add_money(int(input(" Please Deposit to activate your account : ")))

        print(" Account Activated")

        return user.username

    def transactions_view(self):
    
        print(" Please select your desired action below \n")
        print(" A: Instant Transfer    B: Mobile Top-up    \n     C: Check Balance   D:Withdrawal   \n ==>  ")
        action = input()
        return action


    def instant_transfer_view(self, user_id):
        print("please enter your account number")  
        acc = input()
    
        while len(acc) != 10 or acc.isdigit() is False:
            print( " INVALID ACCOUNT NUMBER....please enter the correct account number: \n  ")   
            acc = input()
        else:
            pass
    
        print("please enter amount")
        amt = int(input())

        while amt < 100 or amt > db[user_id]['account balance']:

            if amt < 100:
                print("cannot transfer amount less than #100.......")
                amt = int(input())
            else:
                print("insufficient funds")
                print(" Press 1 to perform another transaction or 2 to quit ")
                action = input()
                if action == "1":
                    return self.transactions_view()

                else:
                    sys.exit()

        else:
            pass

        print("enter secret password to complete transaction")
        pwd = input()

        auth.transaction_auth(pwd, user_id)

        db[user_id]['account balance'] -= amt

        print(f"Transaction complete......\n your main balance is: {db[user_id]['account balance']}")
        print("press 1 to perform another transaction or press 2 to quit")
        Opt = input()
        if Opt == "1":
            return self.transactions_view()
        else:
            sys.exit()

    
    # def Mobile_Top_up(self, user_id):

    #     print("select service provider: A: 9mobile      B: MTN     \nC: Glo      D: Airtel ")
    #     opt = input()
    #     if opt in ["A", "B", "C", "D"]:
    #     print("Maximum amount to recharge: #10,000.00")
    #     print("please enter amount")
    #     amt = int(input())
    #     else:
    #         pass

    #     while amt > 10000 or amt > usersDB[user_id]['account balance']:

    #     if amt > 10000:
    #         print("Maximum amount: #10,000.00")
    #         amt = int(input())
    #     else:
    #         print("insufficient funds")
    #         print(" Press 1 to perform another transaction or 2 to quit ")
    #         action = input()
    #         if action == "1":
    #             return transactions_view()

    #         else:
    #             sys.exit()
                

    #     else:
    #         pass

    #     print("enter secret password to complete transaction")
    #     pwd = input()

    #     verify_pwd(pwd)

    #     usersDB[user_id]['account balance'] -= amt

    #     print(f"Transaction complete......\n your main balance is: {usersDB[user_id]['account balance']}")
    #     print("press 1 to perform another transaction or press 2 to quit")
    #     Opt = input()
    #     if Opt == "1":
    #         return transactions_view()
    #     else:
    #         sys.exit()

    



# def check_balance(user_id):

#     print("enter secret password to check account balance")
#     pwd = input()
#     verify_pwd(pwd)
    
#     print(f"your main balance is: {usersDB[user_id]['account balance']}")

#     print(" Press 1 to perform another transaction or 2 to quit ")
    
#     action = input()
    
#     if action == "1":
#         return transactions_view()

#     else:
#         sys.exit()

# def withdrawal(user_id):  
#     print("enter secret password to continue transaction")
#     pwd = input()
#     verify_pwd(pwd)

#     print("select account: A: Savings account      B: Current account")
#     opts = input()
#     if opts in ["A", "B"]:
#        print("enter amount to withdraw (Maximum amount to withdraw at a time is #20,000.00):")      
       
#     amt = int(input())

#     while amt < 999 or amt > usersDB[user_id]['account balance']:

#         if amt < 999:
#                sys.exit()

#     else:
#         pass  
       
#     usersDB[user_id]['account balance'] -= amt

#     print(f"withdrawal complete......\n your main balance is: {usersDB[user_id]['account balance']}")
#     print("press 1 to perform another transaction or press 2 to quit")
#     Opt = input()
#     if Opt == "1":
#         return transactions_view()
#     else:
#         sys.exit()   print("cannot withdraw amount less than #999.00.......")
#             amt = int(input())
#         else:
#             print("insufficient funds")
#             print(" Press 1 to perform another transaction or 2 to quit ")
#             action = input()
#             if action == "1":
#                 return transactions_view()

#             else: