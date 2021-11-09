import database

db = database.db()

class User():

    def __init__(self, username, email, password, fullname, contact):

        self.username = username
        self.email = email
        self.__password = password
        self.fullname = fullname
        self.contact = contact

    def get_firstname(self):
        return self.fullname.split(" ")[0]

    def get_lastname(self):
        return self.fullname.split(" ")[1]

    def get_pwd(self):
        return self.__password

    # def add_money(self, money: int):
    #     print(f" {money} successfully added to {self.fullname}'s account....")
    #     db[self.username]["account balance"] += money
        
    