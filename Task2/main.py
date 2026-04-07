# This is the Task2 main program
# In this program, Heap and Knapsack are integrated into this program
# Reorder_priority uses MinHeap to find the urgent items to re-order
# Budget_optimizer uses Knapsac to help make decision for maximizing the profit efficiently

from inventory import SmartInventorySystem              # Import the main inventory system from Task 1
from reorder_priority import ReorderPriorityQueue       # Import Heap class for finding the reorder priority
from budget_optimizer import knapsack                   # Import Knapsack for optimizing the profit within the budget

# This menu plugs into the SmartInventorySystem
def task2_menu(system):
    pass
    # This is the entry point part
    # Prints Welcome message
    # Option: 1. View reorder priority (Heap)
    # Option: 2. Opitmize budget (Knapsack)
    # Option: 3. Back to main menu
    # Gets choice

    # if choice == 1, uses Heap to find the reorder priority
    # if choice == 2, uses Knapsak to optimize the budget
    # if choice == 3, end this section
    # if press the wrong button, displays invalid choice

# Main entry point
if __name__ == 'main':
    system = SmartInventorySystem                       # Run Task1 menu
    task2_menu(system)                                  # Run Task2 menu
    