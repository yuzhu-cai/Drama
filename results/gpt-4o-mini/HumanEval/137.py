
def convert_to_float(value):
    """Convert a value to a float, handling both '.' and ',' as decimal points."""
    if isinstance(value, str):
        value = value.replace(',', '.')  # Replace ',' with '.' for float conversion
    return float(value)

def compare_one(a, b):
    # Convert both a and b to floats for comparison
    try:
        a_float = convert_to_float(a)
        b_float = convert_to_float(b)
    except ValueError:
        return None  # If conversion fails, return None

    # Check if the values are equal
    if a_float == b_float:
        return None

    # Return the larger value in its original type
    return a if a_float > b_float else b

# Test cases
print(compare_one(1, 2.5))        # ➞ 2.5
print(compare_one(1, "2,3"))      # ➞ "2,3"
print(compare_one("5,1", "6"))    # ➞ "6"
print(compare_one("1", 1))         # ➞ None
