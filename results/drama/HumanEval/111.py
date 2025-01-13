
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    
    # Step 1: Split the input string into a list of letters
    letters = test.split()
    
    # Step 2: Create a dictionary to count occurrences
    letter_count = {}
    
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    # Step 3: Find the maximum count
    if not letter_count:  # Handle the case of an empty input
        return {}
    
    max_count = max(letter_count.values())
    
    # Step 4: Filter the dictionary to include only letters with the maximum count
    max_letters = {letter: count for letter, count in letter_count.items() if count == max_count}
    
    return max_letters

# Example usage
print(histogram('a b c'))        # Output: {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))      # Output: {'a': 2, 'b': 2}
print(histogram('a b c a b'))    # Output: {'a': 2, 'b': 2}
print(histogram('b b b b a'))    # Output: {'b': 4}
print(histogram(''))              # Output: {}
