# Restaurant_Management_System

1. Authentication:
    User authentication module ensures that only registered users can access the system. It includes:

    Sign Up: Allows new users (Admin/Staff) to register by providing Name, Email, Mobile, and Password. User data is stored securely in respective JSON files (Admin.json or Staff.json).

    Sign In: Validates entered Email and Password against stored data. On successful login, users are granted access based on their role:

        (*) Admin: Full access to menu management.

        (*) Staff: Limited access to view menu and place orders.

    It provides a basic security layer and role-based access control in the system.

2. Database:
    The database system in this project uses JSON files to persistently store various types of structured data. Each file plays a specific role in the functioning of the restaurant system:

       (*) Admin.json: Stores registered admin user credentials and details.

       (*) Staff.json: Stores registered staff user credentials and details.

       (*) menu.json: Maintains food menu items under categories like breakfast, lunch, and dinner with half/full pricing.

       (*) order.json: Stores all order records placed by staff including item name, quantity, price, and customer info.

       (*) bill.json: Maintains billing details generated after orders, including total amount, order ID, and date/time.

       (*) tablebooking.json (if used): Contains data of customers who reserved tables, with booking time and person count.

    These JSON files function as lightweight, file-based databases, allowing CRUD operations without a traditional RDBMS.

3. Domain:
    The Domain module contains the core business logic of the restaurant. It controls how features work together to perform tasks.

    It includes:

    Menu:
        Allows admin to manage the menu by:

           (*) Adding, updating, removing, and viewing menu items.

           (*) Organizes menu into breakfast, lunch, and dinner with half/full prices.

    Order:
        Used by staff to:

           (*) Take customer orders by selecting menu category, items, quantity, and size.

           (*) Stores orders in order.json with unique order ID and timestamp.

    Bill:
        Generates bills based on:

           (*) Order ID.

           (*) Calculates total cost based on selected items and quantities.

           (*) Stores bill details in bill.json.

    Table booking:
        Handles table reservations:

           (*) Staff can book tables with customer name and reservation date/time.

           (*) Records stored in tablebooking.json.
    
    Report:
        This module allows the admin to view detailed, date-wise reports of restaurant operations.

        Features include:

           (*) Shows all orders placed on a specific date.

           (*) Displays:

               (*) Ordered items

               (*) Total bill

               (*) Table number (if booked)

        Helps admin review daily business activities and performance.

    It retrieves and filters data from multiple JSON files (order, bill, booking) based on the selected date.

    The Domain module is the heart of operations and connects user actions to stored data.
4. logs:
    The Logs module is used for error handling and debugging.

    Key functionalities:

       (*) Logs invalid inputs, system errors, or exceptions into a log file.

       (*) Each log entry includes:

          (*)  Error message

           (*) Timestamp

    Logs are stored in text/JSON format for easy review.

    It ensures system robustness and helps in identifying bugs or misuse.