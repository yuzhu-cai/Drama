
def do_algebra(operators, operands):
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
    operators = ['+', '*', '-']
    operands = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    
    # Validate input lengths
    if len(operators) != len(operands) - 1:
        raise ValueError("The number of operators must be one less than the number of operands.")
    
    # Construct the expression
    expression = str(operands[0])
    for i in range(len(operators)):
        expression += f" {operators[i]} {operands[i + 1]}"
    
    # Evaluate the expression
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

# Example usage
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
result = do_algebra(operators, operands)
print(f"The result of the expression is: {result}")  # Output: The result of the expression is: 9
