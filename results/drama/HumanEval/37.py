
def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Step 1: Extract even-index values
    even_index_values = [l[i] for i in range(0, len(l), 2)]
    
    # Step 2: Sort the extracted values
    sorted_even_index_values = sorted(even_index_values)
    
    # Step 3: Create a new list and insert sorted values back into even indices
    new_list = l[:]  # Create a copy of the original list
    for i, value in enumerate(sorted_even_index_values):
        new_list[i * 2] = value  # Insert sorted value back into even index
    
    return new_list

# Example usage
if __name__ == "__main__":
    print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
    print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
    print(sort_even([10, 20, 30, 40, 50, 60]))  # Output: [30, 20, 50, 40]
