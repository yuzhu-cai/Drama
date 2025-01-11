
def by_length(arr):
    # Step 1: Filter the array to keep only integers between 1 and 9
    filtered = [x for x in arr if 1 <= x <= 9]
    
    # Step 2: Sort the filtered array
    filtered.sort()
    
    # Step 3: Reverse the sorted array
    filtered.reverse()
    
    # Step 4: Map each digit to its corresponding name
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [names[x - 1] for x in filtered]  # x - 1 because list is 0-indexed
    
    return result

# Example usage:
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # Output: []
print(by_length([1, -1, 55]))  # Output: ["One"]
