
def count_consonants(word):
    """Helper function to count the number of consonants in a word."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char.isalpha() and char not in vowels)

def select_words(s, n):
    """Returns a list of all words from string s that contain exactly n consonants."""
    if not s:  # Check if the input string is empty
        return []
    
    # Split the string into words
    words = s.split()
    
    # Filter words that have exactly n consonants
    result = [word for word in words if count_consonants(word) == n]
    
    return result

# Example usage
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))      # Output: []
print(select_words("Hello world", 4))              # Output: ["world"]
print(select_words("Uncle sam", 3))                # Output: ["Uncle"]
