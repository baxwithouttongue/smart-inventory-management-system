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

    def get_smallest(self):
        
        pass
    
    def minheapify(self, i):
        pass

class ReorderPriorityQueue:
   pass