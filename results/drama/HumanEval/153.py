
def Strongest_Extension(class_name, extensions):
    """
    Finds the strongest extension based on the given criteria.

    Parameters:
    class_name (str): The name of the class.
    extensions (list): A list of extension names (as strings).

    Returns:
    str: The strongest extension in the format 'ClassName.StrongestExtensionName'.
    """
    strongest_extension = None
    strongest_strength = float('-inf')  # Start with the lowest possible strength

    for ext in extensions:
        # Calculate CAP and SM
        CAP = sum(1 for char in ext if char.isupper())
        SM = sum(1 for char in ext if char.islower())
        
        # Calculate strength
        strength = CAP - SM
        
        # Update strongest extension if the current one is stronger
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = ext

    # Return the result in the required format
    return f"{class_name}.{strongest_extension}" if strongest_extension else None

# Example usage
result = Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])
print(result)  # Output: Slices.SErviNGSliCes

# Another example
result2 = Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
print(result2)  # Output: my_class.AA
