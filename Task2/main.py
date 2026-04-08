# This is the Task2 main program
# In this program, Heap and Knapsack are integrated into this program
# Reorder_priority uses MinHeap to find the urgent items to re-order
# Budget_optimizer uses Knapsac to help make decision for maximizing the profit efficiently

from inventory import SmartInventorySystem                  # Import the main inventory system from Task 1
from reorder_priority import ReorderPriorityQueue           # Import Heap class for finding the reorder priority
from budget_optimizer import knapsack                       # Import Knapsack for optimizing the profit within the budget

# This menu plugs into the SmartInventorySystem
def task2_menu(system):
    while True:                                             # Creates a loop until the user exit the while loop
        print('\n ***** Welcome to Task 2 Menu *****')      # Displays Welcome message
        print('Option: 1. View reorder priority (Heap)')    # Displays option 1: Use Heap to find the highest priority product to reorder
        print('Option: 2. Opitmize budget (Knapsack)')      # Displays option 2: Use Knapsack to maximize the profit within the budget
        print('Option: 3. Back to main menu')               # Displays option 3: Exit Task 2 menu
        choice = input('Enter your option:  ')              # Gets choice

        if choice == '1':                                   # Uses Heap to find the reorder priority
            pass
        
        elif choice == '2':                                 # Uses Knapsak to optimize the budget
            pass
    
        elif choice == '3':                                 # Exits this section
            break

        else:                                               # Wrong entry and displays invalid choice
            print('Invalid choice.')

# Main entry point
if __name__ == '__main__':
    system = SmartInventorySystem()                       # Run Task1 menu
    task2_menu(system)                                  # Run Task2 menu
    