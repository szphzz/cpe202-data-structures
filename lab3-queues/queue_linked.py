class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.back = None
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
        if self.num_items == 0:
            new_node = Node(item)
            self.front = new_node
            self.back = new_node
            self.num_items += 1
        elif self.num_items != self.capacity:
            new_node = Node(item)
            self.back.next = new_node
            self.back = new_node
            self.num_items += 1
        else:
            raise IndexError('queue is full')

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items != 0:
            dequeued = self.front.data
            self.front = self.front.next
            self.num_items -= 1
            return dequeued
        else:
            raise IndexError('queue is empty')

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
