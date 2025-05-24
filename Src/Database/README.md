# Restaurant_Management_System

Database:

    The database system in this project uses JSON files to persistently store various types of structured data. Each file plays a specific role in the functioning of the restaurant system:

       (*) Admin.json: Stores registered admin user credentials and details.

       (*) Staff.json: Stores registered staff user credentials and details.

       (*) menu.json: Maintains food menu items under categories like breakfast, lunch, and dinner with half/full pricing.

       (*) order.json: Stores all order records placed by staff including item name, quantity, price, and customer info.

       (*) bill.json: Maintains billing details generated after orders, including total amount, order ID, and date/time.

       (*) tablebooking.json (if used): Contains data of customers who reserved tables, with booking time and person count.

    These JSON files function as lightweight, file-based databases, allowing CRUD operations without a traditional RDBMS.