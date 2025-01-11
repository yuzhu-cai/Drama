
def prod_signs(arr):
    if not arr:  # Check if the array is empty
        return None
    
    product_of_signs = 1  # Start with the multiplicative identity
    sum_of_magnitudes = 0  # Initialize sum of magnitudes
    
    for num in arr:
        if num > 0:
            product_of_signs *= 1  # Positive number contributes +1 to the product
        elif num < 0:
            product_of_signs *= -1  # Negative number contributes -1 to the product
        else:
            product_of_signs = 0  # Zero makes the product 0
        
        sum_of_magnitudes += abs(num)  # Add the magnitude of the number
    
    return sum_of_magnitudes * product_of_signs  # Return the final result

# Example usage:
print(prod_signs([1, 2, 2, -4]))  # Output: -9
print(prod_signs([0, 1]))          # Output: 0
print(prod_signs([]))              # Output: None
