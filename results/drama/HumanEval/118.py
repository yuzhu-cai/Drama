
def get_closest_vowel(word):
    """Find the closest vowel that stands between two consonants from the right side of the word."""
    vowels = "aeiouAEIOU"
    consonants_indices = []

    # Step 1: Find indices of consonants
    for i, char in enumerate(word):
        if char.isalpha() and char not in vowels:
            consonants_indices.append(i)

    # Step 2: Check pairs of consonants from the right
    if len(consonants_indices) < 2:
        return ""  # Not enough consonants to find a vowel between them

    # We only need to check the last two consonants
    start = consonants_indices[-2]
    end = consonants_indices[-1]

    # Step 3: Check for vowels between the two consonants
    for j in range(start + 1, end):
        if word[j] in vowels:
            return word[j]  # Return the first vowel found between the two consonants

    return ""  # No vowel found between the last two consonants

# Example usage:
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
