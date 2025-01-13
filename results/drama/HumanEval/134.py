
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    # Trim any trailing whitespace
    txt = txt.rstrip()
    
    # Check if the string is empty after trimming
    if not txt:
        return False
    
    # Split the string into words
    words = txt.split()
    
    # Get the last word
    last_word = words[-1]
    
    # Check if the last character of the last word is a letter
    if last_word and last_word[-1].isalpha():
        # Check if the last character is not part of a word
        # It should be followed by a space or be the end of the string
        if len(txt) == len(last_word) + len(txt.rstrip().split()[-2]) + 1:
            return True
        else:
            return False
    return False

# Example usage
print(check_if_last_char_is_a_letter("apple pie"))      # Output: False
print(check_if_last_char_is_a_letter("apple pi e"))     # Output: True
print(check_if_last_char_is_a_letter("apple pi e "))    # Output: False
print(check_if_last_char_is_a_letter(""))                # Output: False
