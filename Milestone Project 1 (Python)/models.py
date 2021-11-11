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


class Admin():

    def __init__(self, adminID, password, email):
        self.__adminID = adminID
        self.__password = password
        self.email = email

    def get_id(self):
        return self.__adminID

    def get_pwd(self):
        return self.__password

    