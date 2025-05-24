import json
import os
import datetime
import getpass

from Src.Domain.Menu.Menu import MenuManager
from Src.Authentication.Writelog import writelogs
from Src.Authentication.Validation import Validator

class signin:
    def __init__(self):
        pass

    def get_signin(self, role):

        role = role.lower()
        
        if role == "admin":
            path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\Admin.json"
        
        elif role == "staff":
            path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\Staff.json"
        
        else:
            print("Invalid role.")
            return

        if not os.path.exists(path):
            print(f"No {role.capitalize()} data found.")
            return

        with open(path, "r") as file:
            try:
                users = json.load(file)
            except Exception as e:
                print("Data corrupted or empty.",e)
                data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs=json.dumps(data,indent=4)
                writelogs(logs)
                return
            
        while True:
            self.email = input("Enter your Email Id: ")
            if Validator.is_valid_email(self.email):
                break
            else:
                print("Invalid email format! Please enter a valid email.")

        while True:
            self.__password = getpass.getpass("Enter your password: ")
            if Validator.is_valid_password(self.__password):
                break
            else:
                print("Password too short! Please try again.")

        for user in users:
            if user["Email"] == self.email and user["Password"] == self.__password:
                print(f"\nSign in successful! Welcome {user['Name']}")
                if role == "admin":
                    print("You have full access.")
                    MenuManager().admin_menu()
                else:
                    MenuManager().staff_menu()
                return
        print("Sign in failed! Invalid credentials.")