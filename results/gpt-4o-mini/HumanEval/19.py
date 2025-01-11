
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping from string representation to integer
    num_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # Split the input string into words
    words = numbers.split()
    
    # Convert words to their corresponding integer values
    num_list = [num_map[word] for word in words]
    
    # Sort the list of integers
    num_list.sort()
    
    # Convert sorted integers back to their string representations
    sorted_words = [list(num_map.keys())[list(num_map.values()).index(num)] for num in num_list]
    
    # Join the sorted words into a single string
    return ' '.join(sorted_words)

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
