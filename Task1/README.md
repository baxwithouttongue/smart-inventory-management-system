# Smart Inventory Management System

# Overview
This is the Smart Inventory Management System. This program demonstrates the OOP-based inventory management system with employee authentication, product information, inventory tracking, supplier KPI evaluation.

# Requirements:
- Python 3.8+
- Pandas

# Installation
Installation Commands
- Windows & Mac (using pip): pip install pandas

# Quick usage:
 
1. Navigate to the project folder:
cd smart-inventory-management-system/Task1

2. Run the program:
python main.py

3. Login with sample name and passwords:
Manager → Garfield / abc123
Supervisor → King / abc456
Assistant → Boo / abc789

4. Available actions:

view --> display product details (view specific product id from 'P001-P023' or 'all')
add --> add a new product
update --> modify existing product details
exit --> quit the program

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

# Documentation
For detailed instructions, go to (Task1/USER_GUIDE.md) for more details