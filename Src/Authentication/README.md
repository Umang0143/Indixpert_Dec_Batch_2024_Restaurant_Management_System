# Restaurant_Management_System

Authentication:

    User authentication module ensures that only registered users can access the system. It includes:

    Sign Up: Allows new users (Admin/Staff) to register by providing Name, Email, Mobile, and Password. User data is stored securely in respective JSON files (Admin.json or Staff.json).

    Sign In: Validates entered Email and Password against stored data. On successful login, users are granted access based on their role:

        (*) Admin: Full access to menu management.

        (*) Staff: Limited access to view menu and place orders.

    It provides a basic security layer and role-based access control in the system.