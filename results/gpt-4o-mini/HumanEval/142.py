
def sum_squares(lst):
    total = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:  # Index is a multiple of 3
            total += value ** 2
        elif index % 4 == 0:  # Index is a multiple of 4 but not a multiple of 3
            total += value ** 3
        else:
            total += value  # No change for other indices
    return total

# Example test cases
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))         # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
