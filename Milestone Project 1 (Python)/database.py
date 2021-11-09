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





