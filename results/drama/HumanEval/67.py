
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket based on the number of apples and oranges.
    
    Parameters:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expressions to find the number of apples and oranges
    apples_match = re.search(r'(\d+)\s*apples?', s)
    oranges_match = re.search(r'(\d+)\s*oranges?', s)

    # Extract the counts, defaulting to 0 if not found
    apples_count = int(apples_match.group(1)) if apples_match else 0
    oranges_count = int(oranges_match.group(1)) if oranges_match else 0

    # Calculate the number of mangoes
    mangoes_count = n - (apples_count + oranges_count)
    
    return mangoes_count

# Example usage
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
