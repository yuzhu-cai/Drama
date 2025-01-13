
def find_max(words):
    """Return the word with the maximum number of unique characters.
    If multiple words have the maximum number of unique characters,
    return the one that comes first in lexicographical order.
    
    Args:
        words (list): A list of strings.
        
    Returns:
        str: The word with the maximum number of unique characters.
    """
    if not words:  # Handle empty list case
        return ""

    max_unique_count = 0
    result_word = ""

    for word in words:
        unique_chars = set(word)  # Create a set of unique characters
        unique_count = len(unique_chars)  # Count unique characters

        # Update if this word has more unique characters or is lexicographically smaller
        if (unique_count > max_unique_count) or (unique_count == max_unique_count and word < result_word):
            max_unique_count = unique_count
            result_word = word

    return result_word

# Example usage:
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))   # Output: "aaaaaaa"
print(find_max([]))                         # Output: ""
