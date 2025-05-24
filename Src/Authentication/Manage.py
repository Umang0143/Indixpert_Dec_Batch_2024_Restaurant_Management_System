import json
import datetime

from Src.Authentication.Sign_in import signin
from Src.Authentication.Sign_up import signup
from Src.Authentication.Writelog import writelogs

class Menu():
    
    def __init__(self):
        self.signuplist=[]

    def menu(self):
        
        while True:
            print(" ")
            print("*" * 31)
            print("*----- Sumang Restaurant -----*")
            print("*" * 31)
            print("1. Sign in")
            print("2. sign up")
            print("0. Exit")
            print("*" * 31)
            try:
                choice=int(input("Enter your choice (0 to 2):- "))
            
            except Exception as e:
                print("\nInvalid input! please enter a number.")
                data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs=json.dumps(data,indent=4)
                writelogs(logs)
                continue

            if choice == 0:
                print("Exit...")
                exit()
            
            elif choice == 1:
                print("\n----- Signin As -----")
                print("1. Admin")
                print("2. Staff")
                print("*" * 20)
                try:
                    login_choice = int(input("Enter your signin type (1 or 2): "))
                    
                    if login_choice == 1:
                        ob = signin()
                        ob.get_signin("admin")
                    elif login_choice == 2:
                        ob = signin()
                        ob.get_signin("staff")
                    else:
                        print("Invalid signin type!")
                
                except Exception as e:
                    print("\nInvalid input! please enter a number.")
                    data={"error":str(e) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    logs=json.dumps(data,indent=4)
                    writelogs(logs)
            
            elif choice == 2:
                ob=signup()
                ob.get_signup()
            
            else:
                print("\nInvalid Choice! Please select from (0 to 2).")