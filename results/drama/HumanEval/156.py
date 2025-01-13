
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= number <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    
    # Define the mapping of integers to Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]
    
    # Initialize the result string
    roman_numeral = ""
    
    # Loop through the values and symbols
    for i in range(len(val)):
        while number >= val[i]:
            roman_numeral += syms[i]  # Append the corresponding symbol
            number -= val[i]  # Decrease number by the value
    
    return roman_numeral

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    assert int_to_mini_roman(19) == 'xix', "Test case 1 failed"
    assert int_to_mini_roman(152) == 'clii', "Test case 2 failed"
    assert int_to_mini_roman(426) == 'cdxxvi', "Test case 3 failed"
    assert int_to_mini_roman(1000) == 'm', "Test case 4 failed"
    assert int_to_mini_roman(1) == 'i', "Test case 5 failed"
    
    print("All test cases passed!")
