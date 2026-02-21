class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

# out of recursion
class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
    
    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head.next == self.head

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  MUST only use the < operator to compare items'''
        new = Node(item)

        if self.is_empty():
            new.next = self.head
            new.prev = self.head
            self.head.next = new
            self.head.prev = new
        else:
            cur = self.head.next
            if cur.item == new.item:
                return False
            while (cur != self.head) and (cur.item < new.item):
                cur = cur.next
                if cur.item == new.item:
                    return False
            new.next = cur
            new.prev = cur.prev
            cur.prev.next = new
            cur.prev = new
        return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        cur = self.head.next
        while cur != self.head:
            if cur.item == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        cur = self.head.next
        i = 0
        while cur != self.head:
            if cur.item == item:
                return i
            i += 1
            cur = cur.next
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if (index < 0) or (index >= self.size()):
            raise IndexError('index is negative or too large')
        cur = self.head.next
        for x in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        return cur.item

    def search_helper(self, node, item):
        if node == self.head:
            return False
        elif item == node.item:
            return True
        else:
            return self.search_helper(node.next, item)

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return(self.search_helper(self.head.next, item))

    def python_list_helper(self, node, lst):
        if node == self.head:
            return lst
        lst.append(node.item)
        return self.python_list_helper(node.next, lst)
    
    def python_list(self): 
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        return self.python_list_helper(self.head.next, [])

    def python_list_reversed_helper(self, node, lst):
        if node == self.head:
            return lst
        lst.append(node.item)
        return self.python_list_reversed_helper(node.prev, lst)
    
    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper(self.head.prev, [])

    def size_helper(self, node):
        if node == self.head:
            return 0
        return 1 + self.size_helper(node.next)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head.next)
