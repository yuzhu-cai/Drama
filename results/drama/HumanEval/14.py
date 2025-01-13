
from typing import List

def all_prefixes(string: str) -> List[str]:
    """Return a list of all prefixes from shortest to longest of the input string.

    A prefix is defined as any substring that starts from the beginning of the string
    and extends to any point within the string.

    Args:
        string (str): The input string for which prefixes are to be generated.

    Returns:
        List[str]: A list containing all prefixes of the input string, ordered from
                    shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
        >>> all_prefixes('hello')
        ['h', 'he', 'hel', 'hell', 'hello']
        >>> all_prefixes('')
        ['']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate through the length of the input string
    for i in range(1, len(string) + 1):
        # Append the substring from the start to the current index
        prefixes.append(string[:i])
    
    return prefixes

# Example usage
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
    print(all_prefixes(''))  # Output: ['']
