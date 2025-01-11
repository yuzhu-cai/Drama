
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the input string into words and spaces
    words = s.split(' ')
    
    # Sort the characters of each word
    sorted_words = []
    for word in words:
        # Sort the characters in the word and join them back
        sorted_word = ''.join(sorted(word))
        sorted_words.append(sorted_word)
    
    # Join the sorted words back with spaces
    result = ' '.join(sorted_words)
    
    return result

# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
