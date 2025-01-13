
import re

def words_string(s):
    """
    Splits a string of words separated by commas or spaces into an array of words.
    
    Args:
    s (str): The input string containing words separated by commas and/or spaces.
    
    Returns:
    list: A list of words without leading or trailing whitespace.
    
    Example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Use regex to split the string by commas and spaces, and strip whitespace from each word
    words = re.split(r'[,\s]+', s.strip())
    return [word for word in words if word]  # Filter out any empty strings

# Test cases to verify the correctness of the function
def test_words_string():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("apple, banana, orange grape, watermelon") == ["apple", "banana", "orange", "grape", "watermelon"]
    assert words_string("   Hello   world! This is a test.   ") == ["Hello", "world!", "This", "is", "a", "test."]
    assert words_string("  ,  ,  ,  ") == []  # Only commas and spaces
    assert words_string("") == []  # Empty string
    assert words_string("word1,word2,word3") == ["word1", "word2", "word3"]  # No spaces
    assert words_string("word1 , word2 , word3") == ["word1", "word2", "word3"]  # Spaces around commas

    print("All test cases passed!")

# Run the test cases
test_words_string()
