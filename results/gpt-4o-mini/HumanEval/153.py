
def Strongest_Extension(class_name, extensions):
    def calculate_strength(extension):
        CAP = sum(1 for char in extension if char.isupper())
        SM = sum(1 for char in extension if char.islower())
        return CAP - SM

    strongest_extension = None
    highest_strength = float('-inf')

    for extension in extensions:
        strength = calculate_strength(extension)
        if strength > highest_strength:
            highest_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

# Example usage:
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
