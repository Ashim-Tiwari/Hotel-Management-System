
# Hotel Management System using tkinter GUI

A brief description of what this project does and who it's for:


## Acknowledgements

- Tribhuwan University, Thapathali Campus.
- Project contributors: Ashim Tiwari, Kshitiz Raj Paudyal.


## Features
### Room Management
- Reserve rooms and check availability.
- Manage room types (Single, Double, Luxury) and display room amenities.

### Customer Management
- Add, update, delete, and search customer details.
- Manage customer ID proofs and contact information.

### Staff Management
- Add, update, delete, and search staff records.
- Assign roles and track employment details (e.g., department, salary, shift).

### Admin Login System
- Secure login system for authorized administrators.
- Protect sensitive data and operations.

### Pages and Interfaces
- **Login Page**: For authentication.
- **Home Page**: Overview of features and navigation.
- **Room Reservation Page**: For booking rooms.
- **Customer Details Page**: Manage customer information.
- **Staff Details Page**: Manage staff records and roles.


## Objectives
- Provide a user-friendly graphical interface for managing hotel activities.
- Simplify room reservation and occupancy tracking.
- Efficiently manage customer and staff information.
- Ensure secure access for administrators.
## API Reference
Since this is a desktop-based application without external APIs, the main interaction occurs between:
- **Python and MySQL** for database queries (e.g., room availability, customer/staff records).
- Internal methods to execute CRUD operations for rooms, customers, and staff.
## Deployment

### Prerequisites
1. Install Python (version >= 3.8).
2. Install MySQL server.
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt



## Steps to deploy


1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   cd hotel-management-system

2. Import the database.sql file into your MySQL server.
3. Update the database credentials in the Python code.
4. Run the application:
    ```bash 
    python main.py



## FAQ

####  What if I get a database connection error?

- Ensure your MySQL server is running.
- Verify the database credentials in the code.

#### Can this system be scaled for multiple users?

Yes, with minor changes to the backend and deployment setup, this system can support multi-user operations.

#### How secure is the admin login system?

The system uses basic password protection but can be enhanced with password hashing and multi-factor authentication.



## Future Enhancements
- Add analytics and reporting dashboards.
- Integrate cloud storage for scalability.
- Create a mobile-friendly version using frameworks like Kivy.
