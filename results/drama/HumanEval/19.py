
from typing import List

def words_to_numbers(word: str) -> int:
    """Convert a single word representation of a number to its integer value."""
    number_map = {
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
    return number_map.get(word.lower(), None)

def numbers_to_words(number: int) -> str:
    """Convert an integer value to its string representation."""
    number_map = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    return number_map.get(number)

def sort_numbers(numbers: str) -> str:
    """Sort a space-delimited string of numeral words from 'zero' to 'nine'.
    
    Args:
        numbers (str): A space-delimited string of numeral words.
        
    Returns:
        str: A space-delimited string of sorted numeral words.
    
    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into words
    words = numbers.split()
    
    # Convert words to their corresponding integer values
    integer_values = [words_to_numbers(word) for word in words]
    
    # Sort the integer values
    sorted_integers = sorted(integer_values)
    
    # Convert sorted integers back to their string representations
    sorted_words = [numbers_to_words(num) for num in sorted_integers]
    
    # Join the sorted words into a single space-delimited string
    result = ' '.join(sorted_words)
    
    return result

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
