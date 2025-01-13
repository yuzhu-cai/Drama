
def exchange(lst1, lst2):
    # Count odd and even numbers in lst1
    odd_count_lst1 = sum(1 for x in lst1 if x % 2 != 0)
    even_count_lst1 = len(lst1) - odd_count_lst1
    
    # Count odd and even numbers in lst2
    odd_count_lst2 = sum(1 for x in lst2 if x % 2 != 0)
    even_count_lst2 = len(lst2) - odd_count_lst2
    
    # If lst1 has no odd numbers, return "YES"
    if odd_count_lst1 == 0:
        return "YES"
    
    # If odd_count_lst1 is even, we can pair them with even numbers from lst2
    if odd_count_lst1 % 2 == 0 and even_count_lst2 > 0:
        return "YES"
    
    # If odd_count_lst1 is odd, we need at least one even number in lst2 to make the last odd even
    if odd_count_lst1 % 2 != 0 and even_count_lst2 > 0:
        return "YES"
    
    # If we don't have enough even numbers in lst2 to replace all odd numbers in lst1
    return "NO"

# Example usage:
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
