# CPE 202 Lab 1

# Data definitions:

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Signature: Maybe_List -> Maybe_integer
# Purpose: Find the value of the largest number
def max_list_iter(int_list):
   '''Finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError'''
   if int_list is None:
      raise ValueError('list is None')
   
   if len(int_list) == 0:
      return None

   int_list.sort()
   return int_list[-1]

# Signature: Maybe_List -> Maybe_List
# Purpose: Return the reverse of the input list 
def reverse_list(int_list):
   '''Returns the reverse of the input list, but does not mutate the input list
   If list is None, raises ValueError'''
   if int_list is None:
      raise ValueError('list is None')
      
   if len(int_list) == 0:
      return []
   
   newlist = []
   for i in range(len(int_list) - 1, -1, -1):
      newlist += [int_list[i]]
   return newlist

# Signature: Maybe_List -> None
# Purpose: Reverse the original input list 
def reverse_list_mutate(int_list):
   '''Reverses a list, modifying the input list
   If list is None, raises ValueError'''
   if int_list is None:
      raise ValueError('list is None')
   
   for i in range(len(int_list) // 2):
      int_list[i], int_list[-1 - i] = int_list[-1 - i], int_list[i]

# Signature: Maybe_List -> Maybe_List
# Purpose: Return the reverse of the input list using recursion
def reverse_rec(int_list):   # must use recursion
   '''Returns the reverse of the input list, but does not mutate the input list.
   May NOT mutate the original list. If list is None, raises ValueError'''
   if (int_list == None):
      raise ValueError('list is None')

   if len(int_list) == 0:
      return []

   newlist = [int_list[-1]] + reverse_rec(int_list[:-1])
   return newlist
