
def convert_to_numeric(value):
    """Convert string representations of numbers to float, handling both '.' and ',' as decimal points."""
    normalized_value = value.replace(',', '.')
    try:
        return float(normalized_value)
    except ValueError:
        return None  # Return None if conversion fails

def compare_one(a, b):
    """
    Compare two values (integers, floats, or strings representing real numbers)
    and return the larger value in its original type. Return None if the values are equal.
    """
    # Convert both values to numeric types if they are strings
    num_a = convert_to_numeric(a) if isinstance(a, str) else a
    num_b = convert_to_numeric(b) if isinstance(b, str) else b

    # If both values are equal, return None
    if num_a == num_b:
        return None

    # Return the larger value in its original type
    return a if num_a > num_b else b

# Example usage:
print(compare_one(1, 2.5))          # Output: 2.5
print(compare_one(1, "2,3"))        # Output: "2,3"
print(compare_one("5,1", "6"))      # Output: "6"
print(compare_one("1", 1))           # Output: None
