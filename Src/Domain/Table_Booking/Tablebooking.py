import os
import json
import datetime
import uuid

from Src.Authentication.Writelog import writelogs

tablebooking_path = fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Database\tablebooking.json"

class TableBooking:
    def __init__(self):
        if not os.path.exists(tablebooking_path):
            with open(tablebooking_path, "w") as file:
                json.dump([], file, indent=4)
        self.total_tables = 10
        self.seats_per_table = 4

    def load_bookings(self):
        with open(tablebooking_path, "r") as file:
            return json.load(file)

    def save_bookings(self, bookings):
        with open(tablebooking_path, "w") as file:
            json.dump(bookings, file, indent=4)

    def display_table_status(self):
        try:
            bookings = self.load_bookings()
            table_status = {str(i): 0 for i in range(1, 11)}  

            for booking in bookings:
                booking_time = datetime.datetime.strptime(booking["booking_time"], "%Y-%m-%d %H:%M:%S")
                if (datetime.datetime.now() - booking_time).total_seconds() <= 7200 and booking["status"] == "active":
                    table_status[booking["table_no"]] += booking["num_people"]

            print("\n--- Table Status ---")
            for table_no, people in table_status.items():
                available_seats = self.seats_per_table - people
                status = "Available" if available_seats > 0 else "Fully Occupied"
                print(f"Table {table_no}: Occupied - {people}, Available - {available_seats} seats ({status})")
            print("--------------------")

        except Exception as e:
            print("Something went wrong while showing table status.")
            writelogs(json.dumps({"error": str(e), "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, indent=4))

    def book_table(self):
        try:
            self.display_table_status()
            table_no = input("Enter table number to book (1 to 10): ").strip()
            if table_no not in [str(i) for i in range(1, self.total_tables + 1)]:
                print("Invalid table number.")
                return

            num_people = int(input("Enter number of people: "))
            if num_people <= 0 or num_people > self.seats_per_table:
                print("Invalid number of people.")
                return

            bookings = self.load_bookings()
            current_occupied = sum(
                int(b["num_people"]) for b in bookings
                if b["table_no"] == table_no and b["status"] == "active" and
                   (datetime.datetime.now() - datetime.datetime.strptime(b["booking_time"], "%Y-%m-%d %H:%M:%S")).total_seconds() <= 7200
            )

            if current_occupied + num_people > self.seats_per_table:
                print(f"Table {table_no} doesn't have enough free seats.")
                return

            booking_data = {
                "booking_id": str(uuid.uuid4())[:6],
                "table_no": table_no,
                "num_people": num_people,
                "status": "active",
                "booking_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            bookings.append(booking_data)
            self.save_bookings(bookings)
            print(f"Table {table_no} booked for {num_people} people.")
            return table_no

        except Exception as e:
            print("Something went wrong while booking the table.")
            writelogs(json.dumps({
                "error": str(e),
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }, indent=4))

    def is_table_valid_and_available(self, table_no):
        try:
            bookings = self.load_bookings()
            now = datetime.datetime.now()
            for b in bookings:
                if b["table_no"] == table_no and b["status"] == "active":
                    booking_time = datetime.datetime.strptime(b["booking_time"], "%Y-%m-%d %H:%M:%S")
                    if (now - booking_time).total_seconds() <= 7200:
                        return True
            return False
        except Exception as e:
            writelogs(json.dumps({"error": str(e), "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, indent=4))
            return False
