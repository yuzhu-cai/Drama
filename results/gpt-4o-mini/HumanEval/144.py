
def simplify(x, n):
    # Split the fractions into numerator and denominator
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))
    
    # Calculate the product of the fractions
    numerator_product = x_numerator * n_numerator
    denominator_product = x_denominator * n_denominator
    
    # Check if the product is a whole number
    return numerator_product % denominator_product == 0

# Test cases
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
