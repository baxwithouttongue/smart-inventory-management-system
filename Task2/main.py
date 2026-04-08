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
            queue = ReorderPriorityQueue()
            for product in system.products:                 # Adds all products
                queue.add_product(product.id, product.stock, product.reorder_point)
            print("Next product to reorder:", queue.get_next_reorder())         # Displays the next product to reorder (minheap pops out the product with the smallest reorder point)
        
        elif choice == '2':                                 # Uses Knapsak to optimize the budget
            budget = int(input('Enter budget: '))           # Asks user for budget
            chosen_products, total_profit = knapsack(system.products, budget)   # Calls the knapsack function with the list of products chosen for purchase
            print('Chosen products: ')                      # Displays the chosen products words

            for prod in chosen_products:                    # Creates a loop to go through each product in the list of chosen products

                # Displays the details of each product (Product ID, Units purchased, Unit cost and unit profit, Total cost and toal profit)
                print(f"  {prod['id']} - Units: {prod['units']}, "
                      f"Unit cost: {prod['unit_cost']}, Unit profit: {prod['unit_profit']}, "
                      f"Total cost: {prod['total_cost']}, Total profit: {prod['total_profit']}")
            print(f'\nTotal profit: {total_profit}')        # Displays the overall profit from all chosen products
    
        elif choice == '3':                                 # Exits this section
            break

        else:                                               # Wrong entry and displays invalid choice
            print('Invalid choice.')

# Main entry point
if __name__ == '__main__':
    system = SmartInventorySystem()                         # Run Task1 menu
    task2_menu(system)                                      # Run Task2 menu
    