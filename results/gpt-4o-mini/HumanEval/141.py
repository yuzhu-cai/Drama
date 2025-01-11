
def file_name_check(file_name):
    """Check if the provided file name is valid based on specific criteria."""
    
    # Split the file name into the name and extension
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    # Check if the name is empty
    if not name:
        return 'No'
    
    # Check if the first character is a letter
    if not name[0].isalpha():
        return 'No'
    
    # Check the extension
    valid_extensions = ['txt', 'exe', 'dll']
    if extension not in valid_extensions:
        return 'No'
    
    # Count the digits in the name
    digit_count = sum(c.isdigit() for c in name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'

# Example usage
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("example123.txt"))  # => 'Yes'
print(file_name_check("example1234.txt"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example."))  # => 'No'
print(file_name_check(".example.txt"))  # => 'No'
print(file_name_check("example.txtx"))  # => 'No'
