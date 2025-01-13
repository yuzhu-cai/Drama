
def total_match(lst1, lst2):
    '''
    This function accepts two lists of strings and returns the list that has 
    a total number of characters in all strings of the list less than the other list.
    
    If the two lists have the same number of characters, it returns the first list.

    Parameters:
    lst1 (list): The first list of strings.
    lst2 (list): The second list of strings.

    Returns:
    list: The list with the smaller total character count, or the first list if counts are equal.
    '''
    # Calculate the total character count for both lists
    count1 = sum(len(item) for item in lst1)
    count2 = sum(len(item) for item in lst2)
    
    # Compare the counts and return the appropriate list
    if count1 < count2:
        return lst1
    else:
        return lst2  # This includes the case where count1 == count2

# Example usage:
print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']
