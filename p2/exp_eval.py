from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

# Too many operands
def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument: a string containing a postfix expression where tokens 
    are space separated. Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    
    lst = token_tests(input_str)
    s = Stack(30)
    num_operands = 0
    
    for tok in lst:
        if isinstance(tok, float) or isinstance(tok, int):
            s.push(tok)
            num_operands += 1
        elif isinstance(tok, str):
            top = s.pop()
            sec_from_top = s.pop()
            s.push(operate(sec_from_top, top, tok))
                
    if num_operands < 2:
        raise PostfixFormatException('Insufficient operands')
    
    return s.pop()
    
def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument: a string containing an infix expression where tokens are 
    space separated. Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression'''
    
    lst = token_tests(input_str)
    s = Stack(30)
    rpn = []

    for tok in lst:
        if is_float_or_int(tok):
            rpn.append(str(tok))
        elif tok == '(':
            s.push(tok)
        elif tok == ')':
            in_par = s.pop()
            while in_par != '(':
                rpn.append(in_par)
                in_par = s.pop()
        else:
            if tok == '**':
                while not s.is_empty() and prec(tok) < prec(s.peek()):
                    rpn.append(s.pop())
            else:
                while not s.is_empty() and prec(tok) <= prec(s.peek()):
                    rpn.append(s.pop())
            s.push(tok)
            
    while not stack.is_empty():
        rpn.append(s.pop())
        
    return ' '.join(rpn)

def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument: a string containing a prefix expression where tokens are 
    space separated. Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    
    lst = token_tests(input_str)
    lst.reverse()
    s = Stack(30)
    
    for tok in lst:
        if is_float_or_int(tok):
            s.push(str(tok))
        else:
            top = s.pop()
            sec_from_top = s.pop()
            res = top + ' ' + sec_from_top + ' ' + tok
            s.push(res)
            
    return s.peek().strip()

def operate(op1, op2, sign):
    if sign == '+':
        comp = op1 + op2
    elif sign == '-':
        comp = op1 - op2
    elif sign == '*':
        comp = op1 * op2
    elif sign == '/':
        if op2 == 0:
            raise ValueError
        comp = op1 / op2
    elif sign == '**':
        comp = op1 ** op2
    elif sign == '>>':
        try:
            comp = op1 >> op2
        except TypeError:
            raise PostfixFormatException('Illegal bit shift operand')
    elif sign == '<<':
        try:
            comp = op1 << op2
        except TypeError: 
            raise PostfixFormatException('Illegal bit shift operand')
        
    return comp        

def is_float_or_int(n):
    try:
        float(n)
        return True
    except TypeError:
        return False

def is_neg_or_pos_int(n):
    if (n[0] == '-') and (n!= '-'):
        return n[1:].isdigit()
    
    return n.isdigit()

def token_tests(input_str):
    valid_input = ['+', '-', '*', '/', '**', '>>', '<<']
    
    if input_str.strip() == '':
        raise PostfixFormatException('Empty input')
    
    lst = [x.strip() for x in input_str.split()]
    for tok in lst:
        if (tok not in valid_input) or (not is_float_or_int(tok)):
            raise PostfixFormatException('Invalid token')

    for i in range(len(lst)):
        if is_neg_or_pos_int(lst[i]):
            lst[i] = int(lst[i])
        elif is_float_or_int(lst[i]):
            lst[i] = float(lst[i])
            
    return lst

def prec(op):
    op_list = ['+', '-', '*', '/', '**', '>>', '<<', '(', ')']
    prec_list = [1, 1, 2, 2, 3, 4, 4, 0, 0]
    return prec_list[op_list.index(op)]
