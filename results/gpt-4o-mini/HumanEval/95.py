
def check_dict_case(d):
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
    if not d:
        return False
    
    # Initialize flags for lower and upper case
    all_lower = True
    all_upper = True
    
    for key in d.keys():
        # Check if the key is a string
        if not isinstance(key, str):
            return False
        
        # Check if the key is lower case
        if key.islower():
            all_upper = False
        # Check if the key is upper case
        elif key.isupper():
            all_lower = False
        else:
            return False  # Mixed case
        
    return all_lower or all_upper

# Example usage
print(check_dict_case({"a": "apple", "b": "banana"}))  # True
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # False
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # False
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))  # False
print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # True
