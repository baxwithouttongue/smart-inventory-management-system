# Defines the Product class
class Product:                                                    # Product class creates a blueprint for creating product objects
    def __init__(self, data):                                     # Creates a constructor method to initialize the instance attributes of the product class
        self.id = str(data['product_id']).strip()                      # Stores the product ID as a string and clean spaces from the beginning and end of a string
        self.product_name = str(data['product_name']).strip()          # Stores the product name as a string, and clean spaces from the beginning and end of a string
        self.price = float(str(data['price (hkd)']).strip())                   # Stores the product price as a float (decimal number)
        self.supplier_name = str(data['supplier_name']).strip()        # Stores the supplier's name as a string, and clean spaces from the beginning and end of the string
        self.stock = int(str(data['stock_level']).strip())                     # Stores the current stock quantity as an integer
        self.safety_stock = int(str(data['safety_stock']).strip())             # Stores the safety stock quantity as an integer
        self.lead_time = int(str(data['lead_time (days)']).strip())                   # Stores the lead time as an integer. This is the days taken between ordering and receiving
        self.ordering_cost = int(str(data['ordering_cost']).strip())           # Stores the ordering cost as an integer. This is the purchasing cost per unit of product
        self.holding_cost = int(str(data['holding_cost']).strip())             # Stores the holding cost as an integer. This is the cost for storing per unit of product
        self.delivered = int(str(data['quantity_delivered']).strip())          # Stores the quantity delivered as an integer. This is the total units delivered
        self.returned = int(str(data['quantity_returned']).strip())            # Stores the quantity returned as an integer. This is the total units returned
        self.priority_value = self.price * self.stock

    
    def supplier_kpi_score(self):                                 # Defines a method to calculate the performance of the supplier based on just simple returned quantity percentage
        if self.delivered == 0:                                   # In case there is no delivery, we still calculate the KPI
            return 100                                            # The supplier's performance should be 100%. No delivery = No returned product = 100% KPI
        else:                                                     # If there is any delivery, we calculate the supplier's KPI based on the returned quantity percentage
            return (1 - self.returned / self.delivered) * 100     # 1 - return rate = good rate = supplier's KPI
        
    def reorder_point(self):
        return self.safety_stock + (self.delivered // max(1, self.lead_time))       # The formula: reorder point = safety stock + (average daily demand × lead time)