import json
import os
import uuid
import datetime

from Src.Authentication.writelogs import writelogs

class signup:
    def __init__(self):
        self.id=id
        self.name=input("Enter your Name:- ")
        self.email=input("Enter your Email Id:- ")
        self.__password=input("Enter your password:- ")
        self.role = input("Enter your Role (Admin/Staff):- ")
    
    def get_signup(self):
        signupdict={}
        signupdict["Id"]=str(uuid.uuid4())[:6]
        signupdict["Name"]=self.name
        signupdict["Email"]=self.email
        signupdict["Password"]=self.__password
        signupdict["Role"] = self.role
        
        if self.role == "admin":
            path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\Admin.json"
        elif self.role == "staff":
            path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\Staff.json"
        else:
            print("Invalid Role!")
            return
        
        if os.path.exists(path):
            with open(path, "r") as file:
                try:
                    signuplist = json.load(file)
                except Exception as e:
                    signuplist = []
                    data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    logs=json.dumps(data,indent=4)
                    writelogs(logs)
        else:
            signuplist = []
        
        signuplist.append(signupdict)
        
        with open(path,"w") as file:
            json.dump(signuplist,file,indent=4)