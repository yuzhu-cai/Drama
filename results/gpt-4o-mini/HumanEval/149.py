
def sorted_list_sum(lst):
    """Filter out strings with odd lengths and return a sorted list."""
    # Step 1: Filter out strings with odd lengths
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    
    # Step 2: Sort the filtered list by length and then alphabetically
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    
    return sorted_list

# Example usage:
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]
