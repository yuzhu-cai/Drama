
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    
    # Start with the first operand
    result = operand[0]
    
    # Iterate through the operators and operands
    for i in range(len(operator)):
        op = operator[i]
        next_operand = operand[i + 1]
        
        # Perform the operation based on the operator
        if op == '+':
            result += next_operand
        elif op == '-':
            result -= next_operand
        elif op == '*':
            result *= next_operand
        elif op == '//':
            result //= next_operand
        elif op == '**':
            result **= next_operand
        else:
            raise ValueError(f"Unsupported operator: {op}")
    
    return result

# Example usage:
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)  # Output: 9
