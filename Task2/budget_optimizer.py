# This is the budget optimizer to implement Knapsack algorithm
# This program tells the user to buy the profitable products as many as possible  under a given budget to provide the highest profit.

def knapsack(products, budget):     # Defines a Knapsak method to choose which products to buy and how many units

    # Calculates and sorts the highest profitability products first to maximize the total profit under the limited budgets
    products.sort(key=lambda p: (p.price - (p.ordering_cost + p.holding_cost)) / (p.ordering_cost + p.holding_cost), reverse=True)

    chosen_products = []            # Creates a list to store the chosen products
    total_profit = 0                # Creates the counter to track the total profit
    remaining_budget = budget       # Creates a variable to track the budget is left for buying the other products

    for p in products:              # Creates a loop to go through all products
        unit_cost = p.ordering_cost + p.holding_cost        # Total cost = ordering cost + inventory holding cost
        unit_profit = p.price - unit_cost                   # Selling price - unit cost = Profit made per unit of product

        if unit_profit <= 0:        # If the product does not make any profit
            continue                # Jumps to the next product in the loop

        max_units = min(p.stock, remaining_budget // unit_cost)     # Determines the maximum units we can buy under the budget. // to give the integer of the units

        if max_units > 0:                                           # Checks if we have enough money to buy at least one unit
            profit = max_units * unit_profit                        # Calculates the maximum profit that i can make under the budget
            cost = max_units * unit_cost                            # Calculates the cost of the units
            remaining_budget -= cost                                # Subtracts the cost from our remaining budget
            total_profit += profit                                  # Adds the profit to the total profit

        # Saves product details, use append
            chosen_products.append({
                'id': p.id,
                'units': max_units,
                'unit_cost': unit_cost,
                'unit_profit': unit_profit,
                'total_cost': cost,
                'total_profit':  profit
            })
    # Sorts the chosen products in a decending order
    
    chosen_products.sort(key = lambda x : x['total_profit'], reverse = True)

    return chosen_products, total_profit


    
        
