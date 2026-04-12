# Task 1: Smart Inventory Management System

# Overview

About the Smart Inventory Management System, this program demonstrates the OOP-based inventory management system with employee authentication, product information, inventory tracking, supplier KPI evaluation.

The system allows to view, add and update the product details. 

Role-based permissions define different levels of permission according to the role of the employee, i.e., a manager, supervisor or an assistant. 

- Manager: view, add, update, exit
- Supervisor: add, view, exit
- Assistant: view, exit

# Requirements:
- Python 3.8+
- Pandas

# Installation
1. Copy or download the repository:
https://github.com/baxwithouttongue/smart-inventory-management-system.git

2. Navigate to the project folder:
```bash
cd smart-inventory-management-system/Task1

3. Installation Commands:
pip install pandas


# Run the program
1. Start the system

python main.py

Then it will display:
Username:
Password:

You can choose the following user to run the program.
__________________________________________________________________________
|   Username    |   Password    |     Role      |       Permissions       |
---------------------------------------------------------------------------
|   Garfield    |   abc123      |   Manager     | view, add, update, exit |
---------------------------------------------------------------------------
|   Supervisor  |   abc456      |   Supervisor  |       view, add, exit   |
---------------------------------------------------------------------------
|   Garfield    |   abc123      |   Assistant   |        view, exit       |
---------------------------------------------------------------------------

Note: The password is case sensitive.

After you have succesful login, the main menu will display:

Welcome message! [ Role: ]

Avaiable actions:
view, add, update, or type 'exit'
Choose action:

# Available actions:
1. View
Choose action: view
Enter Product ID to view or 'all' to view all: 
You can enter Product ID: P001 - P023 to view specific product or enter all to show all products.

For example, enter P001

ID: P001, Name: Smartphone (mid-range), Price: 4500.0 HKD
Supplier: SupplierA, Contact: Chan Wai, Email: chanwai@supplierA.com
Stock: 120, Safety Stock: 20, Lead Time: 7 days
Delivered: 500, Returned: 2, KPI Score: 99.60%

2. Add
Choose action: add

Enter the product information according to the following: Product ID, Product Name, Price (HKD), Supplier, Stock level, Safety stock, Lead time (days), Ordering cost, Holding cost, Quantity delivered, Quantity returned.

For example:

Available actions: 
view, add, update, or type 'exit'
Choose action: add

***** Add New Product *****
Product ID: P024
Product Name: AirPod 4
Price (HKD): 1499
Supplier: Apple
Stock level: 100
Safety Stock level: 10
Lead Time (days): 7
Ordering Cost: 1400
Holding Cost: 20
Quantity delivered: 100
Quantity returned: 0
Product is added successfully!

Note: If there is invalid input (e.g., enter letters into numberic fields), the same field will be asked again.

3. Update

Choose action: update

For example:

Enter Product ID to update: p024
Editable fields: product_name, price, supplier_name, stock_level, safety_stock, lead_time (days), ordering_cost, holding_cost, quantity_delivered, quantity_returned

Which field do you want to change? holding_cost
Enter holding cost: 10
Product updated successfully!

To make sure the data is modified, you can view the product detail again. 

Available actions: 
view, add, update, or type 'exit'
Choose action: view
Enter Product ID to view or 'all' to view all: p024

ID: P024, Name: AirPod 4, Price: 1499.0 HKD
Supplier: Apple, Contact: N/A, Email: N/A
Stock: 100, Safety Stock: 10, Lead Time: 7 days
Delivered: 100, Returned: 0, KPI Score: 100.00%


4. Exit
Choose action: exit

The program exits immediately.

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


# Troubleshooting

1. Invalid input
If you have invalid input (e.g., input letters instead of numbers in price field), the system will display the same price field until you provide the valid value. 

2. Invalid username or password
If you have entered wrong username or password, the system will prompt and ask your username again until your identity is authenticated.

3.Import Pandas
This program requires the pandas library.
You need to run and install pandas to run this program.
Run the following command before starting the program:
```bash
pip install pandas



