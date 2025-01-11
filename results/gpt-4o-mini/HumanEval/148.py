
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if both planets are valid
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the indices of the planets
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Determine the range of indices
    start_index = min(index1, index2) + 1
    end_index = max(index1, index2)
    
    # Get the planets in between
    in_between_planets = planets[start_index:end_index]
    
    return tuple(in_between_planets)

# Example usage:
print(bf("Jupiter", "Neptune"))  # Output: ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))    # Output: ("Venus",)
print(bf("Mercury", "Uranus"))   # Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
