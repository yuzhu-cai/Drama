
def select_words(s, n):
    """Given a string s and a natural number n, return a list of all words from string s 
    that contain exactly n consonants, in the order they appear in the string s.
    If the string s is empty then return an empty list.
    """
    
    if not s:  # Check if the string is empty
        return []
    
    # Helper function to count consonants in a word
    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for char in word if char in consonants)
    
    # Split the string into words
    words = s.split()
    
    # Filter words that have exactly n consonants
    result = [word for word in words if count_consonants(word) == n]
    
    return result

# Example usage:
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))      # Output: []
print(select_words("Hello world", 4))              # Output: ["world"]
print(select_words("Uncle sam", 3))                # Output: ["Uncle"]
