
def compare(game, guess):
    """Compares the actual game scores with the guessed scores and returns the differences.
    
    Args:
    game (list of int): The actual scores of the matches.
    guess (list of int): The guessed scores of the matches.
    
    Returns:
    list of int: A list containing the absolute differences or 0 if guessed correctly.
    """
    result = []
    for actual, guessed in zip(game, guess):
        if actual == guessed:
            result.append(0)
        else:
            result.append(abs(actual - guessed))
    return result

# Example usage:
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]))  # Output: [0, 0, 0, 0, 3, 3]
print(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]))  # Output: [4, 4, 1, 0, 0, 6]
