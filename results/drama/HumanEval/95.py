
def check_dict_case(input_dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    
    # Check if the dictionary is empty
    if not input_dict:
        return False

    # Check if all keys are strings
    if not all(isinstance(key, str) for key in input_dict.keys()):
        return False

    # Check if all keys are lowercase
    all_lower = all(key.islower() for key in input_dict.keys())
    # Check if all keys are uppercase
    all_upper = all(key.isupper() for key in input_dict.keys())

    # Return True if all keys are either lowercase or uppercase
    return all_lower or all_upper

# Example usage:
print(check_dict_case({"a": "apple", "b": "banana"}))  # Output: True
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # Output: False
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # Output: False
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))  # Output: False
print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # Output: True
