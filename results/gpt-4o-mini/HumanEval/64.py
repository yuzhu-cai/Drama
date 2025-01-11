
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Define the set of vowels
    vowels = 'aeiouAEIOU'
    count = 0
    
    # Count the vowels in the string
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        # Check if 'y' is at the end of the string
        elif s[i] == 'y' and i == len(s) - 1:
            count += 1
        elif s[i] == 'Y' and i == len(s) - 1:
            count += 1
            
    return count


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("hello") == 2
    assert vowels_count("sky") == 0
    assert vowels_count("play") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("rhythm") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5
    assert vowels_count("y") == 0
    assert vowels_count("yY") == 1
    assert vowels_count("") == 0
    assert vowels_count("xyz") == 0
    assert vowels_count("a") == 1
    assert vowels_count("yummy") == 2
    assert vowels_count("bY") == 1

    print("All test cases passed!")

# Run the test cases
test_vowels_count()
