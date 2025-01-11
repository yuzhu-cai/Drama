
def fruit_distribution(s, n):
    # Split the string to extract the number of apples and oranges
    parts = s.split()
    
    # Extract the number of apples and oranges
    apples = int(parts[0])  # The first part is the number of apples
    oranges = int(parts[3])  # The fourth part is the number of oranges
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
