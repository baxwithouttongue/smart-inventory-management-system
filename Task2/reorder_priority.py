# This is the reorder_priority program to apply Heap
# To find which item needs to be reordered first
# The item with the smallest reorder_point comes out first

class MinHeap:                     # Creates a MinHeap Class
    def __init__(self):
        self.data = []             # Creates an empty list for storing the heap elements

    def parent(self, i):            # Parenet index
        return (i - 1) //2                       

    def left(self, i):             # Left child index
        return (2 * 1 + 1)

    def right(self, i):            # Right child index
        retrun (2 * i + 2)

    def insert

    def insert(self, key, value):        # Insert a new element into the MinHeap
        self.data.append(key, value)
        i = len(self, data) - 1
        while i > 0 and self.data[(i-1)]//2 > self.data[i]:
            self.data[i], self.data[(i-1)]//2 = self.data[(i-1)//2], self.data[i]
            i = (i - 1)//2

    def get_smallest(self):             # The self.data list stores heap elements
        if not self.data:               # If the list is empty
            return None                 # There is nothing to return
        
        if len(self.data) == 1:         # If there is only one element inside the list
            return self.data.pop()      # Removes and returns to the only element from the list
        
        root = self.data[0]             # In the min-heap, the smallest element is always set as index[0] and stores in the root variable

        self.data[0] = self.data.pop()  # Replaces the root with the last element

        self.minheapify(0)              # Calls the minheapify section
    


        pass
    
    def minheapify(self, i):
        pass

class ReorderPriorityQueue:
   pass