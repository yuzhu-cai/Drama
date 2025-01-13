
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace. 
    If no whitespaces exist in the text, split on commas. 
    If no commas exist, return the number of lower-case letters with odd order in the alphabet 
    (where ord('a') = 0, ord('b') = 1, ..., ord('z') = 25).
    
    Examples:
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") ➞ 3 
    '''
    
    # Check for whitespace
    if ' ' in txt:
        return txt.split()  # Split on whitespace
    # Check for commas if no whitespace is found
    elif ',' in txt:
        return txt.split(',')  # Split on commas
    else:
        # Count lowercase letters in odd positions
        odd_position_letters = {'b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z'}
        count = 0
        
        # Iterate through each character in the string
        for char in txt:
            # Check if the character is a lowercase letter and in the odd position set
            if char in odd_position_letters:
                count += 1
                
        return count  # Return the count of odd-position letters

# Example usage
print(split_words("Hello world!"))  # Output: ["Hello", "world!"]
print(split_words("Hello,world!"))   # Output: ["Hello", "world!"]
print(split_words("abcdef"))          # Output: 3
print(split_words("No commas or spaces"))  # Output: 0
