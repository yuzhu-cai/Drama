
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
    
    # Split the input string into a list of letters
    letters = test.split()
    
    # Create a dictionary to count occurrences
    count_dict = {}
    
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    # Determine the maximum count
    max_count = max(count_dict.values(), default=0)
    
    # Create a new dictionary for letters with the maximum count
    result = {letter: count for letter, count in count_dict.items() if count == max_count}
    
    return result


print(histogram('a b c'))        # Output: {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))      # Output: {'a': 2, 'b': 2}
print(histogram('a b c a b'))    # Output: {'a': 2, 'b': 2}
print(histogram('b b b b a'))    # Output: {'b': 4}
print(histogram(''))              # Output: {}
