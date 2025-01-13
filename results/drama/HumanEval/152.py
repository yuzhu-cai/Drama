
def compare(game, guess):
    """
    Compares the actual scores of matches with the guessed scores.
    
    Parameters:
    game (list): A list of actual scores.
    guess (list): A list of guessed scores.
    
    Returns:
    list: A list of absolute differences between the actual scores and the guessed scores.
          If the guess is correct, the value is 0.
    """
    # Check if both lists are of the same length
    if len(game) != len(guess):
        raise ValueError("Both lists must be of the same length.")
    
    # Create a new list to store the absolute differences
    differences = [abs(g - gs) for g, gs in zip(game, guess)]
    
    return differences

# Example usage:
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]))  # Output: [0, 0, 0, 0, 3, 3]
print(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]))  # Output: [4, 4, 1, 0, 0, 6]
