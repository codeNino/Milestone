import mysql_db_connection as engine
import models
import auth

import sys, time

DB = engine.db()

User = models.User

class User_view():

    def Landing_page(self):
        print(" Serving Nigeria, One Transaction at a time.\n ")
        print("Enter '1' to Login or '2' To Register as a new user!....... \n")
        action = input(" ==>  ")
        while action != "1" and action != "2":
            print("Enter '1' to Login or '2' To Register as a new user!....... \n")
            action = input(" ==>  ")
        else:
            pass
        if action == "1":
            return self.login_page()
        else:
            return self.register_user()


    def login_page(self):
        print("\n Welcome to Charis Bank..\n Please Enter your UserName to proceed ")
        username = input(" ==>  ")
        user_exists = auth.verify_users(username)

        while user_exists == False:

            print(" User Does not Exist....\n Press 1 to try again or Press 2 to Register as a new user or Q to QUIT. ")
            action = input()
    
            while action not in ['1', '2', 'Q']:
                print(" Press 1 to try again or Press 2 to Register as a new user or Q to QUIT. ")
                action = input()
            else:
                pass

            if action == '1':
                print("Please Enter Valid UserID :    ")
                username = input(" ==> ")
                user_exists = auth.verify_users(username)
                if user_exists:
                    break
            elif action == '2':
                username = self.register_user()
                user_exists = auth.verify_users(username)
                if user_exists:
                    break
            else:
                sys.exit()
        else:
            pass

        print(" Please enter your secret password to continue \n")
        pwd = input(" ==> ")

        authenticated = auth.verify_pwd(pwd, username)

        while not authenticated:
            print("Incorrect Password...\n")
            print("Enter '1' to Try again or 'Q' to Quit...")
            action = input(" ==> ")
            while action != "1" and action != "Q":
                print("Incorrect Password...\n")
                print("Enter '1' to Try again or 'Q' to Quit...")
                action = input(" ==> ")
            else:
                pass
            if action == "1":
                print(" Please enter your secret password to continue \n ==> ")
                pwd = input(" ==> ")
                authenticated = auth.verify_pwd(pwd, user_id)
                if authenticated:
                    break
            else:
                sys.exit()

        else:
            user_data = DB.read({"username":username})
            self.__user = User(username, user_data["email"],
                            user_data["password"], user_data["name"],
                            user_data["contact"])
            return self.transactions_view()


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
        while "@" not in email or auth.validate_domain_name(email.split("@")[1]) == False:
            print("Invalid email....\n")
            email = input(" Enter your Email:   ")
        else:
            pass

        contact = input(" Please Enter your Phone Number:   ")
        while all(map(str.isdigit, contact)) is False or len(contact) != 11:
            print("Contact Invalid")
            contact = input("Please Enter Invalid Number:  ")
        else:
            pass

        user = User(username, email, passwd, name, contact)

        deposit = int(input(" Please Deposit to activate your account : "))

        DB.add(user)
        DB.update({"account_balance": deposit}, {"username": username})

        print("You have successfully registered!!")
        print(" Account Activated")

        return self.login_page()

    def transactions_view(self):
        print(f" Welcome {self.__user.get_firstname()} to Charis Bank \n ")
    
        print(" Please select your desired action below \n")
        print(" A: Instant Transfer    B: Mobile Top-up    \n     C: Check Balance   D:Withdrawal  \n  E: QUIT  \n ==>  ")
        action = input()
        while action !="A" and action != "B" and action != "C" and action != "D" and action != "E":
            print(" Please select your desired action below \n")
            print(" A: Instant Transfer    B: Mobile Top-up    \n     C: Check Balance   D:Withdrawal  \n  E: QUIT  \n ==>  ")
            action = input()
        else:
            if action == "E":
                sys.exit()
            else:
                if action == "A":
                    return self.instant_transfer(self.__user.username)
                elif action == "B":
                    return self.Mobile_Top_up(self.__user.username)
                elif action == "C":
                    return self.check_balance(self.__user.username)
                else:
                    return self.withdrawal(self.__user.username)


    def __account_view(self):
        print("select account: A: Savings account      B: Current account   \n  C:  Fixed Deposit ")
        opts = input()
        return True


    def instant_transfer(self, user_id):

        acc_bal = DB.read({"username":user_id})['account_balance']

        Banks = {"A": "FLEMMING BANK", "B": "WEST MIDLANDS BANK", "C" : "REVENANT BANK",
                    "D" : "HOGWARTS BANK", "E" : {"A" : "VIOLET BANK", "B" : "SPARKLING BANK",
                     "C" : "ORANGE BANK",
                    "D" : "REVERE"}}

        self.__account_view()

        print(" Bank to transfer: \n A: FLEMMING BANK     D: HOGWARTS BANK \n B: WEST MIDLANDS BANK     E: OTHERS \n C: REVENANT BANK  \n ==>")
        bank = input()
        while bank not in ["A", "B", "C", "D", "E"]:
            print(" Bank to transfer: \n A: FLEMMING BANK     D: HOGWARTS BANK \n B: WEST MIDLANDS BANK     E: OTHERS \n C: REVENANT BANK  \n ==>")
            bank = input("==>   ")
        else:
            pass
        if bank != "E":
            print(" DESTINATION ACCOUNT NUMBER: \n ==> ")
            acc = input()
            while len(acc) != 10 or acc.isdigit() is False:
                print( " INVALID ACCOUNT NUMBER....PLEASE CHECK AND TRY AGAIN \n  ")
                print(" Enter account number ==>  ")
                acc = input(" ==> ")
            else:
                pass
            print("\n AMOUNT TO TRANSFER ==>   \n")
            amount = int(input("==>  "))

            while amount > 200000 or amount > acc_bal:
                if amount > 200000:
                    print(" Cannot Transfer more than #200 000 ")
                    amount = int(input("Please Enter Amount:   "))
                else:
                    print("Insufficient Funds")
                    print(" Press 1 to perform another transaction or 2 to quit \n ==>    ")
                    action = input()
                    if action == "1":
                        return self.transactions_view()
                    else:
                        sys.exit()
            else:
                pass

            print(" Please Enter Password to continue: \n Password ==>")
            pwd3 = input()

            auth.transaction_auth(pwd3, user_id)

            DB.update({"account_balance": acc_bal - amount}, {"username": user_id}) 
        
            print(f" YOU TRANSFERED {amount} TO USER {acc} AT {bank}  ")
            print(" Press 1 to perform another transaction or 2  to Quit.. \n")
            action = input()
            if action != 1:
                sys.exit()
            else:
                return self.transactions_view()

        else:
            print(" SELECT BANK: \n A: VIOLET BANK        C: ORANGE BANK \n B: SPARKLING BANK        D: REVERE \n ==>")
            bank = Banks["E"][input("  ==>  ")]
            print(" DESTINATION ACCOUNT NUMBER: \n ==> ")
            acc = input()
            while len(acc) != 10 or acc.isdigit() is False:
                print( " INVALID ACCOUNT NUMBER....PLEASE CHECK AND TRY AGAIN \n  ")
                print(" Enter account number ==>  ")
                acc = input()
            else:
                pass
    
        print("Please Enter Amount:  ")
        amount = int(input())

        while amount > 200000 or amount > acc_bal:
            if amount > 200000:
                print(" Cannot Transfer more than #200 000 ")
                amount = int(input("Please Enter Amount:   "))
            else:
                print("Insufficient Funds")
                print(" Press 1 to perform another transaction or 2 to quit \n ==>    ")
                action = input()
                if action == "1":
                    return self.transactions_view()
                else:
                    sys.exit()
        else:
            pass

        print("Please Enter you secret password to complete transaction")
        pwd = input()

        auth.transaction_auth(pwd, user_id)

        DB.update({"account balance": acc_bal - amount}, {"username": user_id} ) 

        print(f"Transaction complete......\n your main balance is: {acc_bal - amount}")
        print("press 1 to perform another transaction or press 2 to quit")
        Opt = input()
        if Opt == "1":
            return self.transactions_view()
        else:
            sys.exit()

    
    def Mobile_Top_up(self, user_id):

        acc_bal = DB.read({"username":user_id})['account_balance']

        print("select service provider: A: 9mobile      B: MTN     \nC: Glo      D: Airtel ")
        input()
        print("Maximum amount to recharge: #10,000.00")
        print("please enter amount")
        amt = int(input())
        while amt > 10000 or amt > acc_bal:
            if amt > 10000:
                print("Maximum amount: #10,000.00")
                amt = int(input("Please Enter Amount:   "))
            else:
                print(" Insufficient Funds ")
                print(" Press 1 to perform another transaction or 2 to quit \n ==>    ")
                action = input()
                if action == "1":
                    return self.transactions_view()
                else:
                    sys.exit()
        else:
            pass

        print("Please Enter secret password to complete transaction\n")
        pwd = input(' ==>   ')

        auth.transaction_auth(pwd, user_id)

        DB.update({"account balance": acc_bal - amt}, {"username": user_id}) 

        print(f"Transaction complete......\n your main balance is: #{acc_bal - amt}")
        print("press 1 to perform another transaction or press 2 to quit")
        Opt = input()
        if Opt == "1":
            return self.transactions_view()
        else:
            sys.exit()

    
    def check_balance(self, user_id):

        self.__account_view()

        time.sleep(2)
    
        print(f"your main balance is: {DB.read({'username':user_id})['account_balance']}")

        print(" Press 1 to perform another transaction or 2 to quit ")
    
        action = input()
    
        if action == "1":
            return self.transactions_view()

        else:
            sys.exit()

    def withdrawal(self, user_id):

        acc_bal = DB.read({'username':user_id})['account_balance']
    
        def amount_to_withdraw_view():
            fund = {"A": 2000, "B": 5000, "C": 10000}
            print(" Select amount to withdraw: \n ")
            print(" A:  2000      C: 10000 \n B: 5000     D: Other Amount \n ==>  ")    
            option = input("==>   ")

            while option not in ["A","B","C","D"]:
                print(" Select amount to withdraw:\n ")
                print(" A:  2000      C: 10000 \n B: 5000     D: Other Amount \n ==>  ")
                option = input()
            else:
                pass

            if option == "A" or option == "B" or option == "C":
                money = fund[option]
                return money

            elif option == "D":
                print("Please Enter amount to withdraw (Not greater than 20 000)")
                money = int(input(" Amount ==>   "))
                while money > 20000:
                    print(" Limit Exceeded....")
                    print(" Please Enter amount not greater than 20000 \n ==> ")
                    money = int(input(" Amount ==>   "))
                else:
                    return money

        self.__account_view()
           
        amt = amount_to_withdraw_view()

        while amt < 1000 or amt > acc_bal:
            if amt < 1000:
                print("Can't Withdraw Amount Less than 1000 ")
                print("Please Enter 1 to try again or 2 to perform another transaction or Q to quit")
                action = input("==>  ")
                if action == "1":
                    amt = amount_to_withdraw_view()
                elif action == "2":
                    return self.transactions_view()
                else:
                    sys.exit()
            else:
                print("Insufficient Funds ")
                print("Please Enter 1 to perform another transaction or Q to quit")
                action = input("==>  ")
                if action == "1":
                    return self.transactions_view()
                else:
                    sys.exit()

        else:
            pass

        print("Please Enter secret password to complete transaction\n")
        pwd = input(' ==>   ')

        auth.transaction_auth(pwd, user_id)
        
        time.sleep(2)

        DB.update({"account balance": acc_bal - amt}, {"username": user_id}) 
        print(f"Please Take your cash......\n your main balance is #{acc_bal - amt}")
        print("press 1 to perform another transaction or press 2 to quit")
        action = input(" ==>  ")
        if Opt == "1":
            return self.transactions_view()
        else:
            sys.exit()