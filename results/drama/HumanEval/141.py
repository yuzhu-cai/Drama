
import re

def count_digits(file_name):
    """Count the number of digits in the file name."""
    return sum(char.isdigit() for char in file_name)

def has_exactly_one_dot(file_name):
    """Check if there is exactly one dot in the file name."""
    return file_name.count('.') == 1

def is_valid_substring_before_dot(file_name):
    """Check if the substring before the dot is valid."""
    parts = file_name.rsplit('.', 1)
    if len(parts) != 2:
        return False
    name_part = parts[0]
    return len(name_part) > 0 and name_part[0].isalpha()

def has_allowed_extension(file_name):
    """Check if the substring after the dot is one of the allowed extensions."""
    allowed_extensions = ['txt', 'exe', 'dll']
    parts = file_name.rsplit('.', 1)
    if len(parts) == 2:
        return parts[1] in allowed_extensions
    return False

def file_name_check(file_name):
    """Check if the file name is valid based on specified criteria."""
    if (count_digits(file_name) > 3 or 
        not has_exactly_one_dot(file_name) or 
        not is_valid_substring_before_dot(file_name) or 
        not has_allowed_extension(file_name)):
        return 'No'
    return 'Yes'

# Example usage
print(file_name_check("example.txt"))  # Output: 'Yes'
print(file_name_check("1example.dll"))  # Output: 'No'
print(file_name_check("valid123.txt"))  # Output: 'Yes'
print(file_name_check("invalid..txt"))   # Output: 'No'
print(file_name_check("example.exe"))    # Output: 'Yes'
print(file_name_check("example.txt1"))   # Output: 'No'
print(file_name_check("example."))        # Output: 'No'
print(file_name_check("example.txt.txt")) # Output: 'No'
