def convert(num, b):
    """ Recursive function that returns a string representing num in the base b """

    if (num < 0) or (type(num) != int): # check that num is a nonnegative int
        raise ValueError('num must be a nonnegative integer')
    
    if (b > 16) or (b < 2) or (type(b) != int): # check that b is an int between 2 and 16
        raise ValueError('b must be an integer between 2 and 16')
    
    con_str = '0123456789ABCDEF' # string with all bases
    
    if num < b: # conversion unnecessary
        return con_str[num]
    else:
        return convert(num//b, b) + con_str[num % b] # recursive call
