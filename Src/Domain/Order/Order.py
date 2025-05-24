import os
import uuid
import datetime
import json

from Src.Authentication.Writelog import writelogs
from Src.Domain.Table_Booking.Tablebooking import TableBooking

class OrderManager:
    def __init__(self):
        self.order_path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\order.json"
        self.menu_path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\menu.json"

    def load_menu(self):
        try:
            with open(self.menu_path, "r") as file:
                return json.load(file)
        except:
            return {}

    def save_order(self, order_data):
        orders = []
        try:
            if os.path.exists(self.order_path):
                with open(self.order_path, "r") as file:
                    orders = json.load(file)
        except Exception as e:
            writelogs(json.dumps({"error": f"Failed to load orders: {str(e)}", "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, indent=4))

        orders.append(order_data)

        try:
            with open(self.order_path, "w") as file:
                json.dump(orders, file, indent=4)
        except Exception as e:
            writelogs(json.dumps({"error": f"Failed to save order: {str(e)}", "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, indent=4))

    def place_order(self):
        try:
            tb = TableBooking()

            print("\n1. Continue with already booked table")
            print("2. Book new table now")
            choice = int(input("Enter your choice (1/2): "))

            table_number = None

            if choice == 1:
                table_number = input("Enter table number: ")
                if not tb.is_table_valid_and_available(table_number):
                    print(f"\u274C Table {table_number} is not booked or booking expired.")
                    return
            elif choice == 2:
                table_number = tb.book_table()
                tb.display_table_status()
                if not tb.is_table_valid_and_available(table_number):
                    print(f"\u274C Table {table_number} is not booked or booking expired.")
                    return
            else:
                print("Invalid choice.")
                return

            menu_data = self.load_menu()
            if not menu_data:
                print("No menu data available.")
                return

            order_items = []

            while True:
                print("\n                   ----- Available Items -----")
                for category, items in menu_data.items():
                    print(f"\n                            {category.upper()}")
                    print("-" * 70)
                    print(f"{'ID':<10}{'Item Name':<30}{'Half Price':<15}{'Full Price':<15}")
                    print("-" * 70)
                    for item in items:
                        print(f"{item['id']:<10}{item['name']:<30}{item['half']:<15}{item['full']:<15}")

                item_name = input("\nEnter item name to order: ").strip()
                matched_item = None
                matched_category = None

                for category, items in menu_data.items():
                    for item in items:
                        if item["name"].lower() == item_name.lower():
                            matched_item = item
                            matched_category = category
                            break
                    if matched_item:
                        break

                if not matched_item:
                    print("Item not found.")
                    continue

                size = input("Enter size (half/full): ").lower()
                if size not in ["half", "full"]:
                    print("Invalid size.")
                    continue

                quantity = input("Enter quantity: ")
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity.")
                    continue
                quantity = int(quantity)

                price = matched_item[size] * quantity

                order_items.append({
                    "item_id": matched_item["id"],
                    "item_name": matched_item["name"],
                    "category": matched_category,
                    "size": size,
                    "quantity": quantity,
                    "price": price
                })

                more = input("Add more items? (y/n): ").lower()
                if more != "y":
                    break

            total_amount = sum(item["price"] for item in order_items)

            order_data = {
                "order_id": str(uuid.uuid4())[:6],
                "table_number": table_number,
                "items": order_items,
                "total_amount": total_amount,
                "order_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.save_order(order_data)
            print("\n\u2705 Order placed successfully!")
            print(f" Total Amount: ₹{total_amount}")

        except Exception as e:
            print("\u274C Something went wrong while placing the order.")
            print("Error:", e)
            error_data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            writelogs(json.dumps(error_data, indent=4))