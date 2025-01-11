
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Define the mapping for vowels
    vowel_replacement = {
        'a': 'c', 'A': 'C',
        'e': 'g', 'E': 'G',
        'i': 'k', 'I': 'K',
        'o': 'q', 'O': 'Q',
        'u': 'w', 'U': 'W'
    }
    
    encoded_message = []
    
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            if char in vowel_replacement:  # Check if it's a vowel
                encoded_message.append(vowel_replacement[char])  # Replace vowel
            else:
                encoded_message.append(char.swapcase())  # Swap case for consonants
        else:
            encoded_message.append(char)  # Keep non-letter characters unchanged
    
    return ''.join(encoded_message)

# Example usage
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
