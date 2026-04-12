# Task 1: Smart Inventory Management System

# Overview

About the Smart Inventory Management System, this program demonstrates the OOP-based inventory management system with employee authentication, product information, inventory tracking, supplier KPI evaluation.

The system allows to view, add and update the product details. Role-based permissions define different levels of permission according to the role of the employee, i.e., a manager, supervisor or an assistant. Manager can view, add and update. Supervisor can add and view and assistant can view only.

# Project Folder Contents

Task1
|-- Project_Report.pdf
|-- main.py         # Entry point
|-- product.py      # Product class
|-- supplier.py     # Supplier class
|-- employee.py     # Employee class
|-- inventory.py    # System integration
|-- README.md
|-- USER_GUIDE.md
|-- csv 
    |-- employee_role.csv   # Employee Name, password and roles
    |-- products.csv        # Products information
    |-- suppliers.csv       # Supplier information
    |-- supplier_KPI.csv    # Supplier KPI definition

# Requirements:
- Python 3.8+
- Pandas

# Installation
Installation Commands
- Windows & Mac (using pip): pip install pandas

# Quick usage:
 
1. Navigate to the project folder:
cd smart-inventory-management-system/Task1

2. How to run the program:
python main.py

3. Main Menu
When you run main.py, you will see:
Username:

4. To test all available actions, you can enter:
Username: Garfield
Password: abc123

Manager: Garfield, password: abc123, available action: view, add, update, exit
Supervisor: King, password: abc456, available action: view, add, exit
Assistant: Boo, password: abc789, available action: view, exit

5. Available actions:
Available actions:
View, add, update, or type 'exit'
Choose action: 

Action meaning:

- view --> display the product with specific product ID (fromm P001 to P023) or all
- add --> add a new product
- update --> modify details of an existing product
- exit --> quit the program

6. Invalid input
If you have invalid input (e.g., input letters instead of numbers in price field), the system will display the same price field until you provide the valid value. 

7. Exit
The program will still run until you choose 'exit'.


