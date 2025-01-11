
def find_max(words):
    """Return the word with the maximum number of unique characters.
    If multiple words have the same maximum number of unique characters,
    return the one that comes first in lexicographical order.
    """
    max_word = ""
    max_unique_count = 0

    for word in words:
        unique_chars = set(word)  # Get unique characters in the word
        unique_count = len(unique_chars)  # Count of unique characters

        # Check if this word has more unique characters or is lexicographically smaller
        if (unique_count > max_unique_count) or (unique_count == max_unique_count and word < max_word):
            max_word = word
            max_unique_count = unique_count

    return max_word

# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))   # Output: "aaaaaaa"
