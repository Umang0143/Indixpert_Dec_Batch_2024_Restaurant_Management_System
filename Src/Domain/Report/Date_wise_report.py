import json
import os
import datetime

from Src.Authentication.Writelog import writelogs

bill_file = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\bill.json"

class ReportManager:
    def __init__(self):
        if not os.path.exists(bill_file):
            with open(bill_file, 'w') as file:
                json.dump([], file, indent=4)

    def load_bills(self):
        with open(bill_file, 'r') as file:
            return json.load(file)
    
    def Report_menu(self):
        while True:
            print("\n========= REPORT MENU =========")
            print("1. Report by Date")
            print("2. Report by Table")
            print("3. All Bills Report")
            print("0. Exit")
            try:
                choice = int(input("Enter choice (0 to 3) :- "))

                if choice == 1:
                    self.report_by_date()
                elif choice == 2:
                    self.report_by_table()
                elif choice == 3:
                    self.report_all_bills()
                elif choice == 0:
                    print("Exiting report... ")
                    break
                else:
                    print("Invalid choice. Try again.")
            except Exception as e:
                print("\nInvalid input! Please enter a valid number.")
                data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                logs = json.dumps(data, indent=4)
                writelogs(logs)
                

    def report_by_date(self):
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except Exception as e:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
            data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            logs = json.dumps(data, indent=4)
            writelogs(logs)
            return
        bills = self.load_bills()
        matched = [b for b in bills if b['bill_time'].startswith(date)]

        if not matched:
            print("\nNo records found for the given date.")
            return

        print("\n     ========= Daily Report =========")
        total = 0
        for b in matched:
            print(f"\nTable: {b['table_number']} | Bill ID: {b['bill_id']} | Total: ₹{b['total_amount']} | Payment: {b['payment_method']} | Time: {b['bill_time']}")
            print("Orders:")
            for item in b.get('orders', []):
                name = item.get('item_name', 'N/A')
                qty = item.get('quantity', 0)
                size = item.get('size', '')
                price = item.get('price', 0)
                print(f" - {name} ({size}) x {qty} = ₹{price}")
            total += b['total_amount']
        print(f"\nTotal Revenue for {date}: ₹{total}")

    def report_by_table(self):
        table = input("Enter table number: ")
        bills = self.load_bills()
        matched = [b for b in bills if b['table_number'] == table]

        if not matched:
            print("\nNo records for this table.")
            return

        print(f"\n     ====== Report for Table {table} ======")
        total = 0
        for b in matched:
            print(f"\nTable: {b['table_number']} | Bill ID: {b['bill_id']} | Total: ₹{b['total_amount']} | Payment: {b['payment_method']} | Time: {b['bill_time']}")
            print("Orders:")
            for item in b.get('orders', []):
                name = item.get('item_name', 'N/A')
                qty = item.get('quantity', 0)
                size = item.get('size', '')
                price = item.get('price', 0)
                print(f" - {name} ({size}) x {qty} = ₹{price}")
            total += b['total_amount']
        print(f"\nTotal for Table {table}: ₹{total}")

    def report_all_bills(self):
        bills = self.load_bills()
        if not bills:
            print("\nNo bills available.")
            return

        print("\n     ========= All Bills Summary =========")
        for b in sorted(bills, key=lambda x: x['bill_time'], reverse=True):
            print(f"\nBill ID: {b['bill_id']} | Table: {b['table_number']} | Amount: ₹{b['total_amount']} | Paid: ₹{b['paid_amount']} | Method: {b['payment_method']} | Time: {b['bill_time']}")
            print("Orders:")
            for item in b.get('orders', []):
                name = item.get('item_name', 'N/A')
                qty = item.get('quantity', 0)
                size = item.get('size', '')
                price = item.get('price', 0)
                print(f" - {name} ({size}) x {qty} = ₹{price}")