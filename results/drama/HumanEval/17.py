
from typing import List

def parse_music(music_string: str) -> List[int]:
    """ 
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats each
    note lasts.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    
    # Mapping of note representations to beat values
    note_to_beat = {
        'o': 4,    # Whole note
        'o|': 2,   # Half note
        '.|': 1    # Quarter note
    }
    
    # Split the music_string into individual notes
    notes = music_string.split()
    
    # Convert notes to their corresponding beat values
    beat_values = [note_to_beat[note] for note in notes if note in note_to_beat]
    
    return beat_values

# Example usage
result = parse_music('o o| .| o| o| .| .| .| .| o o')
print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
