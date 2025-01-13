
def encode(message):
    """
    Encodes the message by swapping case and replacing vowels.
    
    Parameters:
    message (str): The input message to encode.
    
    Returns:
    str: The encoded message.
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    
    # Define the mapping for vowels to letters 2 places ahead
    vowel_mapping = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
        'A': 'C',
        'E': 'G',
        'I': 'K',
        'O': 'Q',
        'U': 'W'
    }
    
    # Initialize an empty list to build the encoded message
    encoded_message = []
    
    # Iterate through each character in the message
    for char in message:
        # Swap case
        swapped_char = char.swapcase()
        # Replace vowel if it's in the mapping
        if swapped_char in vowel_mapping:
            encoded_message.append(vowel_mapping[swapped_char])
        else:
            encoded_message.append(swapped_char)
    
    # Join the list into a final string and return
    return ''.join(encoded_message)

# Example usage
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
