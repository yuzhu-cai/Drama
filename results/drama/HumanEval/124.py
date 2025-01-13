
def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False.
    
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1, 3, 5, 7, 8, 10, 12.
       The number of days is not less than 1 or higher than 30 days for months 4, 6, 9, 11.
       The number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy.
    
    Args:
        date (str): The date string to validate.
    
    Returns:
        bool: True if the date is valid, otherwise False.
    """
    
    # Check if the date string is empty
    if not date:
        return False
    
    # Check if the date is in the correct format
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    
    # Split the date string into parts
    month_str, day_str, year_str = date.split('-')
    
    # Validate month, day, and year parts
    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
    except ValueError:
        return False  # If conversion fails, return False
    
    # Validate month
    if month < 1 or month > 12:
        return False
    
    # Validate day based on the month
    if month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:  # Months with 30 days
        if day < 1 or day > 30:
            return False
    elif month == 2:  # February
        if day < 1 or day > 29:  # Allowing for leap years
            return False
    
    # If all checks pass, return True
    return True

# Example usage
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
