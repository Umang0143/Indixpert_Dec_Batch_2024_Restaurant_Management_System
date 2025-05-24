import json
import os
import uuid
import datetime

from Src.Authentication.Writelog import writelogs
from Src.Authentication.Validation import Validator

class signup:
    def __init__(self):
        self.path=fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\Staff.json"
        self.id=id
        while True:
            self.name = input("Enter your Name:- ")
            if Validator.is_valid_name(self.name):
                break
            else:
                print("Invalid name! Only alphabets are allowed.")
        while True:
            self.email = input("Enter your Email Id:- ")
            if Validator.is_valid_email(self.email):
                break
            else:
                print("Invalid email format!")
        while True:
            self.contact = input("Enter your Contact no.:- ")
            if Validator.is_valid_contact(self.contact):
                break
            else:
                print("Invalid contact number! It must be 10 digits.")
        while True:
            self.address = input("Enter your Address:- ")
            if Validator.is_valid_address(self.address):
                break
            else:
                print("Invalid address! It cannot be empty.")
        
        self.__password=Validator.get_valid_password()
        self.role = "staff"
    
    def get_signup(self):
        try:
            signupdict={}
            signupdict["Id"]=str(uuid.uuid4())[:6]
            signupdict["Name"]=self.name
            signupdict["Email"]=self.email
            signupdict["Contact"]=self.contact
            signupdict["Address"]=self.address
            signupdict["Password"]=self.__password
            signupdict["Role"] = self.role
        except:
            data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            logs=json.dumps(data,indent=4)
            writelogs(logs)
        
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
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
        
        with open(self.path,"w") as file:
            json.dump(signuplist,file,indent=4)