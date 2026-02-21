""" class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.back = -1
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        
        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        
        if self.num_items == self.capacity:
            raise IndexError('queue is full')
        elif self.num_items == 0:
            self.items[self.front] = item
            self.back = 1
            self.num_items += 1
        elif self.back == self.capacity - 1:
            self.back = 0
            self.items[self.back] = item
            self.num_items += 1
        elif self.back < self.capacity:
            self.items[self.back] = item
            self.back += 1
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''

        if self.num_items == 0:
            raise IndexError('queue is empty')
        elif self.num_items != 0:
            val = self.items[self.front]
            self.items[self.front] = None
            self.front += 1
            self.back -= 1
            self.num_items -= 1
            return val

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items """

class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.items = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.back = 0
        self.numItems = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return not bool(self.numItems)


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.capacity == self.numItems


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        self.items[self.back] = item
        if self.back == self.capacity - 1:
            self.back = 0
        else:
            self.back += 1
        self.numItems += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        data = self.items[self.front]
        if self.front == self.capacity - 1:
            self.front = 0
        else:
            self.front += 1
        self.numItems -= 1
        return data


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.numItems
