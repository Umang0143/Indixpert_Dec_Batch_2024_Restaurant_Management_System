import json
import os
import datetime
import uuid

from Src.Authentication.Writelog import writelogs

order_file = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\order.json"
bill_file = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\bill.json"

class BillManager:
    def __init__(self):
        if not os.path.exists(bill_file):
            with open(bill_file, 'w') as file:
                json.dump([], file, indent=4)

    def load_orders(self):
        with open(order_file, 'r') as file:
            return json.load(file)

    def save_bill(self, bill):
        with open(bill_file, 'r') as file:
            bills = json.load(file)
        bills.append(bill)
        with open(bill_file, 'w') as file:
            json.dump(bills, file, indent=4)

    def generate_invoice(self):
        try:
            table_no = input("Enter table number for bill generation: ")
            orders = self.load_orders()
            table_orders = [o for o in orders if o['table_number'] == table_no]

            if not table_orders:
                print("\nNo orders found for this table.")
                return

            total_amount = 0
            all_items = []
            print("\n               =========== INVOICE ===========")
            print(f"Table Number: {table_no}")
            print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 60)
            print(f"{'Item':<20}{'Qty':<15}{'Size':<15}{'Price':<15}")
            print("-" * 60)

            for order in table_orders:
                for item in order['items']:
                    print(f"{item['item_name']:<20}{item['quantity']:<15}{item['size']:<15}{item['price']:<15}")
                    all_items.append(item)
                total_amount += order['total_amount']

            print("-" * 60)
            print(f"Total Amount: ₹{total_amount:.2f}")
            print("=" * 60)

            print("\nSelect payment method:")
            print("1. UPI\n2. Cash\n3. Card")
            method_choice = input("Enter choice (1/2/3): ")
            payment_method = {
                "1": "UPI",
                "2": "Cash",
                "3": "Card"
            }.get(method_choice, "Unknown")

            while True:
                try:
                    paid_amount = float(input("Enter payment amount: ₹"))
                    if paid_amount < total_amount:
                        print(f"Insufficient payment. Please pay at least ₹{total_amount:.2f}.")
                    else:
                        break
                except Exception as e:
                    print("Invalid amount. Please enter a valid number.")
                    error_data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    writelogs(json.dumps(error_data, indent=4))

            transaction_id = input("Enter payment reference number: ")

            bill_data = {
                "bill_id": str(uuid.uuid4())[:6],
                "table_number": table_no,
                "total_amount": total_amount,
                "paid_amount": paid_amount,
                "payment_method": payment_method,
                "transaction_id": transaction_id,
                "bill_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "orders": all_items
            }
            self.save_bill(bill_data)
            print("\nPayment successful and bill saved!")

        except Exception as e:
            print(f"Error generating invoice")
            error_data = {"error": str(e), "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            writelogs(json.dumps(error_data, indent=4))