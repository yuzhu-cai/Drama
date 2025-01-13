
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Given a string representing a sentence, return a string that contains the words
    from the original sentence whose lengths are prime numbers.
    The order of the words in the new string should be the same as the original one.
    
    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words based on prime length
    filtered_words = [word for word in words if is_prime(len(word))]
    
    # Join the filtered words back into a single string
    result_string = ' '.join(filtered_words)
    
    return result_string

# Example usage
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
