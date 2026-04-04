# Define the Product class

class Product:
    def __init__(self, data):
        self.id = data['product_id'].strip()                        # Product id
        self.product_name = data['product_name'].strip()            # Product name
        self.price = float(data['price (HKD)']).strip()             # Product price
        self.supplier_name = data['supplier_name'].strip()          # Supplier name
        self.stock = int(data['stock_level']).strip()               # Stock level
        self.safety_stock = int(data['safety_stock']).strip()       # Safety stock level
        self.lead_time = int(data['lead_time']).strip()             # Lead time
        self.ordering_cost = int(data['ordering_cost']).strip()     # Ordering cost
        self.holding_cost = int(data['holding_cost']).strip()       # Holding cost
        self.delivered = int(data['quantity_delivered']).strip()    # Quantity delivered
        self.returned = int(data['quantity_returned']).strip()      # Quantity returned
        self.priority_value = self.price * self.stock


    def supplier_kpi_score(self):
        if self.delivered == 0:                         # In case there is no delivery, we will still calculate the KPI
            return 100                                  # The supplier's performance should be 100%. No delivery = No returned product = 100% KPI
        else:                                           # If there is any delivery, we will calculate the KPI based on the returned quantity percentage
            return (1 - self.returned / self.delivered) * 100
        
    def reorder_point(self):
        pass