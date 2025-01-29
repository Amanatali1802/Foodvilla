# FOODVILLA

FOODVILLA is a Python-based food ordering and management system that provides functionalities for:
- **Database Management** using MySQL
- **Binary File Handling** using Pickle
- **CSV File Handling** for customer data storage

## Features

### 1. Database Management (MySQL)
- Create a database (`FOODVILLA`)
- Create a `MENU` table
- Insert meal orders dynamically
- Display stored meal orders

### 2. Binary File Handling (Pickle)
- Store customer details in a binary file (`food.dat`)
- Read and display stored customer details
- Update customer details
- Delete customer details

### 3. CSV File Handling
- Store customer details in a CSV file (`foodvilla.csv`)
- Read and display stored customer details
- Update customer records
- Delete customer records

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- MySQL Server
- Required Python libraries

### Required Libraries
Install necessary dependencies using:
```sh
pip install mysql-connector-python
```

## How to Run the Project
1. Start the MySQL server.
2. Update the MySQL credentials (`host`, `user`, `password`) in `get_db_connection()`.
3. Run the script:
```sh
python foodvilla.py
```

## Usage
- Navigate through the **Main Menu** to choose between Database, Binary, or CSV operations.
- Follow on-screen instructions to create, insert, update, delete, or view records.



