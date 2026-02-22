import math


def is_prime(n):
    ''' Returns True if n is prime, False otherwise.'''
    if n <= 1:  # edge cases
        return False
    if n <= 3:
        return True
    if (n % 2 == 0) or (n % 3 == 0):  # so can skip middle 5 numbers in loop below
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
    return True

class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will
            be used, if 11 is passed, 11 will be used.)'''
        if is_prime(table_size):
            self.length = table_size
        else:
            self.length = self.next_prime(table_size)
        self.array = [None] * self.length
        self.num_items = 0

    def insert(self, key, value=None):
        hash_val = self.horner_hash(key)
        i = 0
        while i < self.length:
            index = (hash_val + i ** 2) % self.length
            if self.array[index] is None:
                self.array[index] = [key, value]
                self.num_items += 1
                break
            elif self.array[index][0] == key:
                self.array[index] = [key, value]
                break
            i += 1

        if self.get_load_factor() > 0.5:  # rehash
            self.num_items = 0  # reset
            lst_keys = self.get_all_keys()
            lst_pairs = []
            for k in lst_keys:
                lst_pairs.append([k, self.get_value(k)])

            self.length = self.next_prime(self.length * 2)
            self.array = [None] * self.length
            for p in lst_pairs:
                self.insert(p[0], p[1])

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.'''
        n = min(len(key), 8)
        lst_char = list(key)
        hash_val = 0
        i = 0
        while i <= (n - 1):
            horner = ord(lst_char[i]) * 31 ** (n - 1 - i)
            hash_val += horner
            i += 1
        return hash_val

    def next_prime(self, n):
        ''' Find the next prime number that is > n.'''
        if n <= 1: # base case
            return 2

        prime = n
        found = False
        while not found: # loop until is_prime returns True
            prime += 1
            if is_prime(prime):
                found = True
        return prime

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        if self.get_index(key) is not None:
            return True
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None.'''
        hash_val = self.horner_hash(key)
        i = 0
        while i < self.length:
            index = (hash_val + i ** 2) % self.length
            if self.array[index] is None:
                return None
            elif self.array[index][0] == key:
                return index
            else:
                i += 1

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        lst = []
        for i in self.array:
            if i is not None:
                lst.append(i[0])
        return lst

    def get_value(self, key):
        ''' Returns the value associated with the key.
        If key is not in hash table, returns None.'''
        if not self.in_table(key):
            return None
        index = self.get_index(key)
        return self.array[index][1]

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.length

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.length