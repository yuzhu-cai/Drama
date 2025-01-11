
def check_if_last_char_is_a_letter(txt):
    # Trim any trailing whitespace
    txt = txt.rstrip()
    
    # Check if the string is empty after trimming
    if not txt:
        return False
    
    # Get the last character
    last_char = txt[-1]
    
    # Check if the last character is a letter
    if last_char.isalpha():
        # Check if it's not part of a word (i.e., it should be preceded by a space or be the first character)
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    
    return False

# Test cases
print(check_if_last_char_is_a_letter("apple pie"))      # ➞ False
print(check_if_last_char_is_a_letter("apple pi e"))     # ➞ True
print(check_if_last_char_is_a_letter("apple pi e "))    # ➞ False
print(check_if_last_char_is_a_letter(""))                # ➞ False
