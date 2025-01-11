
def closest_integer(value):
    # Convert the input string to a float
    num = float(value)
    
    # Use the built-in round function to get the closest integer
    rounded = round(num)
    
    # Check if the number is equidistant from two integers
    if abs(num - rounded) == 0.5:
        # If num is positive and equidistant, round away from zero
        if num > 0:
            return rounded + 1
        # If num is negative and equidistant, round away from zero
        else:
            return rounded - 1
    
    return rounded

# Test cases
print(closest_integer("10"))     # Output: 10
print(closest_integer("15.3"))   # Output: 15
print(closest_integer("14.5"))   # Output: 15
print(closest_integer("-14.5"))  # Output: -15
print(closest_integer("0.5"))    # Output: 1
print(closest_integer("-0.5"))   # Output: -1
