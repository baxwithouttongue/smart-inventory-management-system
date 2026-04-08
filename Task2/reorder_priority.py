# This is the reorder_priority program to apply MinHeap Data Structure
# To find which item needs to be reordered first
# The item with the smallest reorder_point comes out first

class MinHeap:                              # Creates a MinHeap Class
    def __init__(self):
        self.data = []                      # Creates an empty list for storing the heap elements

    def parent(self, i):                    # Parenet index
        return (i - 1) //2                       

    def left(self, i):                      # Left child index
        return (2 * i + 1)

    def right(self, i):                     # Right child index
        return (2 * i + 2)

    def insert(self, key, value):           # Defines a method to insert a new element into the MinHeap
        self.data.append((key, value))      # Adds the new element to key (priority value), value (the data being stored)
        i = len(self.data) - 1              # Gets the index of the added element
        while i > 0:                        # Creates a loop when index 0 has not been reached
            parent_idx = (i - 1)//2                  # Calculates teh parent index of the current node
            if self.data[parent_idx][0] <= self.data[i][0]:      # If the parent ≤ child, heap stops
                break                       # Exits the loops (arent ≤ child)
            else:                           # If parent > child
                self.data[i], self.data[parent_idx] = self.data[parent_idx], self.data[i]     # Swaps the parent and child
                i = parent_idx                       # Updates i to the parent's index and the loop continues
            
    def get_smallest(self):                 # The self.data list stores heap elements
        if not self.data:                   # If the list is empty
            return None                     # There is nothing to return
        
        if len(self.data) == 1:             # If there is only one element inside the list
            return self.data.pop()          # Removes and returns to the only element from the list
        
        root = self.data[0]                 # In the min-heap, the smallest element is always set as index[0] and stores in the root variable
        self.data[0] = self.data.pop()      # Replaces the root with the last element
        self.minHeapify(0, len(self.data))  # Calls the minheapify section
        return root

    
    def minHeapify(self, i, n):            # Defines a method, i is the root of the subtree, n is the currect size of the heap elements

        smallest = i                        # Assumes the node at index i is the smallest
        left = 2 * i + 1                    # Left child is stored in index[i] at 2 * i + 1. If i = 0, left child index = 1
        right = 2 * i + 2                   # Right child is stored in index [i] at 2 * 1 + 2. if i = 0, then right child index = 2
    
        if left < n and self.data[left][0] < self.data[smallest][0]:            # If left child exists and its priority is less than the current smallest node
            smallest = left                                                     # The left child becomes the new smallest node
        
        if right < n and self.data[right][0] < self.data[smallest][0]:          # If right child exists and its priority is less than the current smallest node
            smallest = right                                                    # The right child becomes the new smallest node
        
        if smallest == i:                                                       # Base case, stops if no swap is needed
            return
        
        self.data[i], self.data[smallest] = self.data[smallest], self.data[i]   # Recursive steps: Swaps the two values to move the smallest value up to position i
        self.minHeapify(smallest, n)        # Calls minHeepfy function recursively to continue the function until base case is met

class ReorderPriorityQueue:                                                     # Defines a class for priority queue for reordering
    def __init__(self):                                                         # Craetes a constructor to create the objects
        self.heap = MinHeap()                                                   # Creates an empty MinHeap (priority queue) object and stores it in self.heap

    def add_product(self, product_id, stock, reorder_point):                    # Defines a method to add a product to the priority queue                       
        self.heap.insert(reorder_point, (product_id, stock))                    # Inserts the product and stores to the priority queue

    def get_next_reorder(self):                                                 # Defines a method to remove and return the most smallest reorder point from the priority queue
        item = self.heap.get_smallest()                                          # Removes and returns the smallest item from the heap. 
        if item:                                                                # Checks the following conditions
            key, (product_id, stock) = item                                     # If the items gets the reorder point, product_id and stock get the values
            return f'{product_id} (stock={stock}, reorder_point={key})'         # Displays which product to reorder
        return None                                                         # If there no product are waiting to be reordered, then return None
