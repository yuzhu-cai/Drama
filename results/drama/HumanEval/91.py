
import re

def is_bored(S):
    """
    Count the number of sentences that start with the word "I".
    
    A sentence is defined as a sequence of words ending with '.', '?', or '!'.
    
    Parameters:
    S (str): The input string containing sentences.
    
    Returns:
    int: The count of sentences that start with the word "I".
    
    Examples:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    >>> is_bored("I am happy! Are you? I enjoy coding.")
    2
    """
    # Split the input string into sentences using regex to account for multiple delimiters
    sentences = re.split(r'(?<=[.!?]) +', S.strip())
    
    # Count the number of sentences that start with 'I'
    count = sum(1 for sentence in sentences if sentence.strip().startswith('I'))
    
    return count

# Example usage
if __name__ == "__main__":
    print(is_bored("Hello world"))  # Output: 0
    print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
    print(is_bored("I am happy! Are you? I enjoy coding."))  # Output: 2
