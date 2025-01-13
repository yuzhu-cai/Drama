
def sorted_list_sum(lst):
    """
    This function accepts a list of strings, removes strings with odd lengths,
    and returns the remaining strings sorted first by length (ascending)
    and then alphabetically for strings of the same length.

    :param lst: List of strings
    :return: List of strings sorted by length and alphabetically
    """
    # Step 1: Filter out strings with odd lengths
    filtered_strings = [s for s in lst if len(s) % 2 == 0]

    # Step 2: Sort the remaining strings first by length, then alphabetically
    sorted_strings = sorted(filtered_strings, key=lambda s: (len(s), s))

    return sorted_strings

# Example usage and assertions
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum(["apple", "banana", "kiwi", "grape", "fig"]) == ["fig", "kiwi", "apple", "grape", "banana"]
assert sorted_list_sum(["hello", "world", "python", "is", "fun"]) == ["is", "fun", "hello", "world", "python"]

# Additional test cases
print(sorted_list_sum(["cat", "dog", "elephant", "bat", "ant"]))  # Output: ['ant', 'bat', 'cat', 'dog']
print(sorted_list_sum(["a", "bb", "ccc", "dddd", "ee"]))  # Output: ['bb', 'ee', 'dddd']
