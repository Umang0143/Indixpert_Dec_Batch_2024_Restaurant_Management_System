# Restaurant_Management_System

Domain:   
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