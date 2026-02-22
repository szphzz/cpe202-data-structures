class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.heap = [None] * (self.capacity + 1)
        self.size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        else:
            self.heap[self.size + 1] = item
            self.size += 1
            self.perc_up(self.size)
            return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        else:
            return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None
        else:
            max = self.heap[1]
            self.heap[1] = self.heap[self.size]
            del self.heap[self.size]
            self.size -= 1
            self.perc_down(1)
            return max

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap[1:self.size + 1]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction. Do NOT call enqueue
        if len(alist) > self.capacity: # adjust heap cap if necessary
            self.capacity = len(alist)
        self.heap = [None] * (self.capacity + 1)

        curr = 1
        for i in alist:
            self.heap[curr] = i
            curr += 1
        self.size = len(alist)

        i = len(alist) // 2 # start with last parent
        while i > 0: # stop at root
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        if self.size == 0:
            return True
        return False

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        if self.size == self.capacity:
            return True
        return False
        
    def get_capacity(self):
        '''this is the maximum number of entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size
        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while (i * 2) <= self.size: # until leaves
            mc = self.max_child(i)
            if (self.heap[i] is not None) and (self.heap[mc] is not None) and (self.heap[i] < self.heap[mc]): # curr is less than one of its children
                tmp = self.heap[i] # swap
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc # move down

    def max_child(self, i):
        '''returns pos of maximum child'''
        if (2 * i + 1 > self.size) or (self.heap[2 * i] > self.heap[2 * i + 1]):
            return 2 * i
        elif self.heap[2 * i] < self.heap[2 * i + 1]:
            return 2 * i + 1

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 > 0: # until root
            if (self.heap[i // 2] is not None) and (self.heap[i] is not None) and (self.heap[i // 2] < self.heap[i]): # if parent is less than curr
                tmp = self.heap[i // 2] # swap
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2 # move up

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        new_list = []
        for i in range(len(alist)):
            val = self.dequeue()
            new_list.append(val)

        curr = 0
        pos = -1
        for i in alist:
            alist[curr] = new_list[pos]
            curr += 1
            pos -= 1