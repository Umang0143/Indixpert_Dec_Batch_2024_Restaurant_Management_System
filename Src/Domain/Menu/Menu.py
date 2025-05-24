import json
import os
import datetime
import uuid
from Src.Authentication.Writelog import writelogs
from Src.Domain.Order.Order import OrderManager
from Src.Domain.Table_Booking.Tablebooking import TableBooking
from Src.Domain.Bill.Bill import BillManager
from Src.Domain.Report.Date_wise_report import ReportManager

menu_path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\menu.json"

class MenuManager:
    def __init__(self):
        default_categories = {"breakfast": [], "lunch": [], "dinner": [], "dessert": [], "beverage": []}
        
        if not os.path.exists(menu_path):
            with open(menu_path, "w") as file:
                json.dump(default_categories, file, indent=4)
        else:
            with open(menu_path, "r") as file:
                try:
                    menu_data = json.load(file)
                except Exception as e:
                    menu_data = {}
                    print("\nInvalid input! Please enter a valid number.")
                    data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    logs = json.dumps(data, indent=4)
                    writelogs(logs)
            updated = False
            for key in default_categories:
                if key not in menu_data:
                    menu_data[key] = []
                    updated = True

            if updated:
                with open(menu_path, "w") as file:
                    json.dump(menu_data, file, indent=4)

    def load_menu(self):
        with open(menu_path, "r") as file:
            return json.load(file)

    def save_menu(self, menu_data):
        with open(menu_path, "w") as file:
            json.dump(menu_data, file, indent=4)

    def get_category(self):
        while True:
            print("\n----- Select Category -----")
            print("1. Breakfast")
            print("2. Lunch")
            print("3. Dinner")
            print("4. Dessert")
            print("5. Beverage")
            print("0. Exit")
            print("*"*27)
            try:
                option = int(input("Enter category option (0 to 5): "))
                if option == 1:
                    return "breakfast"
                elif option == 2:
                    return "lunch"
                elif option == 3:
                    return "dinner"
                elif option == 4:
                    return "dessert"
                elif option == 5:
                    return "beverage"
                elif option == 0:
                    print("Exiting Menu Manager...")
                    return None
                else:
                    print("\nInvalid option. Please try again.")
            except Exception as e:
                print("\nInvalid input! Please enter a valid number.")
                data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs = json.dumps(data, indent=4)
                writelogs(logs)

    def add_item(self):        
        menu_data = self.load_menu()
        category = self.get_category()
        if category is None:
            return

        item = {}
        item["id"] = str(uuid.uuid4())[:6]
        item["name"] = input("Enter item name: ")
        item["half"] = float(input("Enter half price: "))
        item["full"] = float(input("Enter full price: "))

        menu_data[category].append(item)
        self.save_menu(menu_data)
        print("Item added successfully.")

    def update_item(self):
        menu_data = self.load_menu()
        category = self.get_category()
        if category is None:
            return

        items = menu_data[category]
        if not items:
            print("No items found in this category.")
            return

        name = input("Enter item name to update: ")

        found = False
        for item in items:
            if item["name"].lower() == name.lower():
                item["name"] = input("Enter new item name: ")
                item["half"] = float(input("Enter new half price: "))
                item["full"] = float(input("Enter new full price: "))
                self.save_menu(menu_data)
                print("Item updated successfully.")
                found = True
                return   

        if not found:
            print(f"{name} not found in {category}.")

    def remove_item(self):
        menu_data = self.load_menu()
        category = self.get_category()
        if category is None:
            return

        items = menu_data[category]
        if not items:
            print("No items to remove.")
            return

        name = input("Enter item name to remove: ")
        found = False
        for item in items:
            if item["name"].lower() == name.lower():
                menu_data[category].remove(item)
                self.save_menu(menu_data)
                print(f"{item['name']} removed successfully")
                found = True
                return

        if not found:
            print(f"{name} not found")

    def view_menu(self):
        menu_data = self.load_menu()
        print("\n                   ---------- Menu ----------")

        for category, items in menu_data.items():
            print("\n" + f"              ---------- {category.upper()} MENU ----------")
            print("-" * 70)
            if not items:
                print("No items available.")
            else:
                print(f"{'ID':<10}{'Item Name':<30}{'Half Price':<15}{'Full Price':<15}")
                print("-" * 70)
                for item in items:
                    print(f"{item['id']:<10}{item['name']:<30}{item['half']:<15}{item['full']:<15}")

    def admin_menu(self):
        while True:
            print("\n----- Admin Menu Management -----")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Remove Item")
            print("4. View Menu")
            print("0. Exit")
            print("*" * 33)
            try:
                choice = int(input("Enter your choice (0 to 4):- "))
                if choice == 1:
                    self.add_item()
                elif choice == 2:
                    self.update_item()
                elif choice == 3:
                    self.remove_item()
                elif choice == 4:
                    self.view_menu()
                elif choice == 0:
                    print("Exiting Admin Menu...")
                    break
                else:
                    print("\nInvalid choice. Try again.")
            except Exception as e:
                print("\nInvalid input! Please enter a valid number.")
                data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs = json.dumps(data, indent=4)
                writelogs(logs)

    def staff_menu(self):
        while True:
            print("\n----- Staff Menu -----")
            print("1. View Menu")
            print("2. Place Order")
            print("3. Book Table")
            print("4. Generate Bill")
            print("5. View Date-Wise Report")
            print("0. Exit")
            print("*" * 27)
            try:    
                choice = int(input("Enter your choice (0 to 5):- "))
                if choice == 1:
                    self.view_menu()
                elif choice == 2:
                    order = OrderManager()
                    order.place_order()
                elif choice == 3:
                    table=TableBooking()
                    table.book_table()
                elif choice == 4:
                    bill=BillManager()
                    bill.generate_invoice()
                elif choice == 5:
                    report=ReportManager()
                    report.Report_menu()
                elif choice == 0:
                    print("Exiting Staff Menu...")
                    break
                else:
                    print("\nInvalid choice. Try again.")
            except Exception as e:
                print("\nInvalid input! Please enter a valid number.")
                data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs = json.dumps(data, indent=4)
                writelogs(logs)