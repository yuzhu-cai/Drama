
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of cars.
    
    Args:
    n (int): The number of cars in each direction (left to right and right to left).
    
    Returns:
    int: The total number of collisions.
    """
    return n * n  # Each car in one direction collides with each car in the other direction


print(car_race_collision(3))  # Output: 9
print(car_race_collision(5))  # Output: 25
