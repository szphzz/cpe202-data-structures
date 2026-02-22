def bears(n):
    """ Given n bears, I can give back bears following three rules.
I win when I end up with 42 bears (True return value).
If it is impossible to end with 42 bears, False is returned. """
    
    if n == 42: # goal
        return True
    
    if n < 42: # no longer possible to win
        return False

    if n % 2 == 0: # first rule
        n -= n/2
        bears(n)
        return True
    
    elif (n % 3 == 0) or (n % 4 == 0): # second rule
        last = n % 10 
        sec_last = (n % 100)/10
        
        while last * sec_last != 0: # if multiply to 0, move on
            n -= last * sec_last
            bears(n)
            return True
        
    elif n % 5 == 0: # third rule
        n -= 42
        bears(n)
        return True
    
    else: # when none of the above 
        return False
