
def anti_shuffle(s):
    """
    Takes a string and returns an ordered version of it.
    The ordered version of the string is where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.
    Note: The order of words and blank spaces in the sentence is preserved.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the string into words and spaces
    words = s.split()
    spaces = []
    last_index = 0

    # Collect the spaces and their positions
    for char in s:
        if char == ' ':
            spaces.append(last_index)
        last_index += 1

    # Sort the characters in each word
    sorted_words = [''.join(sorted(word)) for word in words]

    # Reconstruct the string
    result = []
    word_index = 0
    for i in range(len(s)):
        if i in spaces:
            result.append(' ')
        else:
            if word_index < len(sorted_words):
                result.append(sorted_words[word_index])
                word_index += 1

    return ''.join(result)

# Example usage
print(anti_shuffle('Hi'))                  # Output: 'Hi'
print(anti_shuffle('hello'))               # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))      # Output: 'Hello !!!Wdlor'
print(anti_shuffle('the quick brown  fox jumps over  lazy dog'))  # Output: 'eht ciku bnorw  fox jmps oerv  alyz dgo'
