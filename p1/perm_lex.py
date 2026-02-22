def perm_gen_lex(str_in):
    
    """ Assuming the input string consists of 0 or more unique lower-case letters
in alphabetical order, return a list of strings, where each string is a permutation. """

    if len(str_in) == 0: # base case of empty string
        return []
    
    if len(str_in) == 1: # base case of string with one char
        return[str_in]

    newlist = []
    for i, v in enumerate(str_in):  # enter recursive loop
        newlist += [v + p for p in perm_gen_lex(str_in[:i] + str_in[i+1:])] # removes char before more recursion
    return newlist
