
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    >>> is_bored("I am bored! Are you? I want to go home.")
    2
    """
    # Split the string into sentences using the specified delimiters
    import re
    sentences = re.split(r'[.!?]', S)
    
    # Initialize a counter for boredoms
    boredom_count = 0
    
    # Check each sentence
    for sentence in sentences:
        # Strip leading/trailing whitespace
        stripped_sentence = sentence.strip()
        # Check if the sentence starts with "I"
        if stripped_sentence.startswith("I"):
            boredom_count += 1
            
    return boredom_count

# Example usage
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
print(is_bored("I am bored! Are you? I want to go home."))  # Output: 2
