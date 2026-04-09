# This is the main entry point for the Smart Inventory Management System
# Import the SmartInventorySystem class from inventory.py
import os
print("Current working directory:", os.getcwd())       # Checks where Python is looking for my CSVs

from inventory import SmartInventorySystem

if __name__ == "__main__":
    system = SmartInventorySystem()     # Create an inventory management system instance
    system.start_system()               # Run the system