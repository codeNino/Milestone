# db = {'Tope75': {"name": "Tope Oke", "password": "Topepompin67",
#  "email": "topeoke@nhubfondation.org", "contact": "08177509782", "account balance": 10000},
#           "Emma419": {"name": "Emmanuel James", "password": "Emmaforthemoney900",
#           "email": "emmanueljames@nhubfoundation.org", "contact": "09054799258", "account balance": 50000},
#           "Ken_drik": {"name": "Kenneth James", "password": "Kendrick500",
#           "email": "kennethjames@nhubfoundation.org", "contact": "07098457234", "account balance": 5000}
#        
#       }

import json
import os

db_path = os.path.abspath(r"C:\Users\lordn\Documents\Programming\Milestone Projects\Milestone Project 1 (Python)\db.txt")

class db():
   
   def query(self, UserID: str):
      with open(db_path, 'r') as f:
         opened_file = f.readlines() 
         if opened_file == "":
            f.close()
            return None
         else:
            data = {} 
            for line in opened_file:
               data.update(dict(json.loads(line)))
               f.close()
            return data.get(UserID, None)
           
            
   def add(self, User: dict):
      with open(db_path, 'r+') as f:
         if f.read() == "":
            json.dump(User, f)
            f.close()
         else:
            f.write("\n")
            json.dump(User, f)
            f.close()





