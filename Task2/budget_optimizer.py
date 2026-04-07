# This is the budget optimizer to implement Knapsack algorithm
# This program tells the user to buy the profitable products as many as possible  under a given budget to provide the highest profit.

def knapsack(products, budget):     # Defines a Knapsak method to choose which products to buy and how many units
    chosen = []                     # Creates a list to store the chosen products
    total_profit = 0                # Creates the counter to track the total profit
    remaining_budget = budget       # Creates a variable to track the budget is left for buying the other products

    for p in products:              # Creates a loop to go through all products
        unit_cost = p.ordering_cost + p.holding_cost        # Total cost = ordering cost + inventory holding cost
        unit_profit = p.price - unit_cost                   # Selling price - unit cost = Profit made per unit of product

        if unit_profit <= 0:        # If the product does not make any profit
            continue                # Jumps to the next product in the loop

        max_units = min(p.stock, remaining_budget // unit_cost)     # Determines the maximum units we can buy under the budget. // to give the integer of the units

        # profit = max_units * unit_profit
        # cost = max_units * unit_cost
        # remaining budget -= cost
        # total profit += profit

        # saves product details, use append

        # sorts the chosen products in a decending order


    
        
