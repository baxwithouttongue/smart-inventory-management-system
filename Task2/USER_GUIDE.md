# Task 2: Smart Inventory Management System


# Overview

To the extension of the Task 1 project, a further exploration to apply a new data structure and a new algorithm to solve real-life problems.  

Heap is the tree-based structure that maintains the maximum or minimum at the root. In the Smart Inventory Management System, reorder priority can be further explored by Min-Heap by keeping the product with the smallest element reorder point at the root. It is to find the most urgent item to reorder.

The Knapsack algorithm is used to utilize the budget to find the best combination of products and quantity to maximize the total profit.


# Requirements:

- Python 3.7+
- Pandas


# Installation

1. Copy or download the repository:
https://github.com/baxwithouttongue/smart-inventory-management-system.git

2. Navigate to the project folder:
```bash
cd smart-inventory-management-system/Task2

3. Installation Commands:
pip install pandas


# Run the program

1. Start the system

python main.py

In order to provide a quick access, there is no username and password needed for this program execution.

Then it will display:

***** Welcome to Task 2 Menu *****
Option: 1. View reorder priority (Heap)
Option: 2. Opitmize budget (Knapsack)
Option: 3. Exit
Enter your option:


# How to use

Option 1 (Reorder Priority)(Heap)
Purpose: It is to find the most urgent item to reorder.

***** Welcome to Task 2 Menu *****
Option: 1. View reorder priority (Heap)
Option: 2. Opitmize budget (Knapsack)
Option: 3. Exit
Enter your option:  1
Next product to reorder: P021 (stock=30, reorder_point=20)
Press Enter to continue.


Option 2: Opitmize budget (Knapsack)
Purpose: it utilizes the budget to find the best combination of products and quantity to maximize the total profit.

For example: budget = 5000
***** Welcome to Task 2 Menu *****
Option: 1. View reorder priority (Heap)
Option: 2. Opitmize budget (Knapsack)
Option: 3. Exit
Enter your option:  2
Enter budget: 5000
Chosen products: 
  p023 - Units: 100, Unit cost: 31, Unit profit: 169.0, Total cost: 3100, Total profit: 16900.0
  p022 - Units: 17, Unit cost: 109, Unit profit: 481.0, Total cost: 1853, Total profit: 8177.0

Total profit: 25077.0
Total budget used: 4953
Remaining budget: 47

You can enter different budget to see different results. 

For example: budget = 50000
***** Welcome to Task 2 Menu *****
Option: 1. View reorder priority (Heap)
Option: 2. Opitmize budget (Knapsack)
Option: 3. Exit
Enter your option:  2
Enter budget: 50000
Chosen products: 
  P003 - Units: 9, Unit cost: 4031, Unit profit: 8769.0, Total cost: 36279, Total profit: 78921.0
  p023 - Units: 100, Unit cost: 31, Unit profit: 169.0, Total cost: 3100, Total profit: 16900.0
  P021 - Units: 30, Unit cost: 155, Unit profit: 495.0, Total cost: 4650, Total profit: 14850.0
  p022 - Units: 30, Unit cost: 109, Unit profit: 481.0, Total cost: 3270, Total profit: 14430.0
  P007 - Units: 3, Unit cost: 812, Unit profit: 988.0, Total cost: 2436, Total profit: 2964.0

Total profit: 128065.0
Total budget used: 49735
Remaining budget: 265

3. Exit

 ***** Welcome to Task 2 Menu *****
Option: 1. View reorder priority (Heap)
Option: 2. Opitmize budget (Knapsack)
Option: 3. Exit
Enter your option:  3

The program exits immediately.


# Project Folder Contents

SMART-INVENTORY-MANAGEMENT-SYSTEM
|
Task2
    |
    |-- main.py         # Entry point
    |-- reorder_priority.py # Reorder Priority by Min-Heap Application
    |-- budget_optimzer.py  # Budget Optimizer by Knapsack Algorithm
    |-- product.py      # Product class
    |-- supplier.py     # Supplier class
    |-- employee.py     # Employee class
    |-- inventory.py    # System integration
    |-- README.md       # Quick orientation
    |-- USER_GUIDE.md   # User Manual
    |-- Study_Report.pdf  # Study Report Task 2
    |-- csv 
        |-- employee_role.csv   # Employee Name, password and roles
        |-- products.csv        # Products information
        |-- suppliers.csv       # Supplier information
        |-- supplier_KPI.csv    # Supplier KPI definition



# Troubleshooting

1. Invalid input
If you have invalid input (e.g., input letters instead of numbers), the system will display the invalid choice.
 ***** Welcome to Task 2 Menu *****
Option: 1. View reorder priority (Heap)
Option: 2. Opitmize budget (Knapsack)
Option: 3. Exit
Enter your option:  R
Invalid choice. 


2.Import Pandas
This program requires the pandas library.
You need to run and install pandas to run this program.
Run the following command before starting the program:
```bash
pip install pandas



