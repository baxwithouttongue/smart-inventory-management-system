# This is the budget optimizer to implement Knapsack algorithm
# This program tells the user to buy the profitable products as many as possible  under a given budget to provide the highest profit.

def knapsack(products, budget):     # Defines a Knapsak method to choose which products to buy and how many units
    chosen = []                     # Creates a list to store the chosen products
    total_profit = 0                # Creates the counter to track the total profit
    remaining_budget = budget       # Creates a variable to track the budget is left for buying the other products

    for p in products:              # Creates a loop to go through all products
        unit_cost = p.ordering_cost + p.holding_cost        # Total cost = ordering cost + inventory holding cost
        unit_profit = p.price - unit_cost                   # Selling price - unit cost = Profit made per unit of product
        
