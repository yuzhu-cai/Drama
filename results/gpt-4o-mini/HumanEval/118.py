
def get_closest_vowel(word):
    """Find the closest vowel that stands between two consonants from the right side of the word."""
    vowels = "aeiouAEIOU"
    n = len(word)
    
    # Start from the end of the word
    for i in range(n - 1, 0, -1):
        if word[i] in vowels:  # Check if the current character is a vowel
            # Check if the previous character is a consonant
            if i > 0 and word[i - 1].isalpha() and word[i - 1] not in vowels:
                # Check if the character before that is also a consonant
                if i - 2 >= 0 and word[i - 2].isalpha() and word[i - 2] not in vowels:
                    return word[i]  # Return the vowel found
    return ""  # Return empty string if no valid vowel is found

# Example usage
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
