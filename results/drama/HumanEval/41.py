
def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of cars.
    
    Parameters:
    n (int): The number of cars in each set.
    
    Returns:
    int: The total number of collisions.
    """
    # Each car in set A collides with each car in set B
    total_collisions = n * n
    return total_collisions

# Example usage
number_of_cars = 5
print(f"Total collisions for {number_of_cars} cars: {car_race_collision(number_of_cars)}")
