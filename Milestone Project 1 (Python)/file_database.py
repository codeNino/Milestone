import json
import os

db_path = os.path.abspath(r"C:\Users\lordn\Milestone Projects\Milestone Project 1 (Python)\userDB.txt")

class db():
   
   def read(self, UserID: str):
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
      try:
         assert type(User) is dict
         with open(db_path, 'r+') as f:
            if f.read() == "":
               json.dump(User, f)
               f.close()
            else:
               f.write("\n")
               json.dump(User, f)
               f.close()
      except AssertionError:
         print(f"Type <User> must be <dict> ")
      except:
         print("Oops! Something Happened")


   def delete(self, UserID: str):
      try:
         with open(db_path, 'r') as f:
            opened_file = f.readlines()
            f.close()
            with open(db_path, 'w') as fw:
               for line in opened_file:
                  if list(dict(json.loads(line)).keys())[0] != UserID:
                     fw.write(line)
               fw.close()
      except:
         print("Oops!! Something went wrong")

   def update(self, UserID: str, data: dict):
      try:
         with open(db_path, 'r') as f:
            opened_file = f.readlines()
            f.close()
            with open(db_path, 'w') as fw:
               for line in opened_file:
                  if list(dict(json.loads(line)).keys())[0] != UserID:
                     fw.write(line)
                  else:
                     doc = dict(json.loads(line))
                     doc[UserID][list(data.keys())[0]] = list(data.values())[0]
                     with open(db_path, 'r') as fc:
                        if fc.read() == "":
                           json.dump(doc, fw)
                        else:
                           fw.write("\n")
                           json.dump(doc, fw)
                        fc.close()
               fw.close()
      except:
         print("Oops!! Something Happened")
