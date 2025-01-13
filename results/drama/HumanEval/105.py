
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    """
    # List of names corresponding to digits 1-9
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    
    # Step 1: Filter the array to include only integers between 1 and 9
    filtered_array = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    
    # Step 2: Sort the filtered array
    sorted_array = sorted(filtered_array)
    
    # Step 3: Reverse the sorted array
    reversed_array = sorted_array[::-1]
    
    # Step 4: Map each digit to its corresponding name
    mapped_names = [names[digit - 1] for digit in reversed_array]
    
    return mapped_names

# Example usage
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # Output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([]))  # Output: []
print(by_length([1, -1, 55]))  # Output: ['One']
