
def eat(number, need, remaining):
    # Calculate how many more carrots the rabbit can eat
    can_eat = min(need, remaining)
    
    # Update the total number of eaten carrots
    total_eaten = number + can_eat
    
    # Update the remaining carrots
    remaining_after_meal = remaining - can_eat
    
    return [total_eaten, remaining_after_meal]

# Example usage:
print(eat(5, 6, 10))  # Output: [11, 4]
print(eat(4, 8, 9))   # Output: [12, 1]
print(eat(1, 10, 10)) # Output: [11, 0]
print(eat(2, 11, 5))  # Output: [7, 0]
