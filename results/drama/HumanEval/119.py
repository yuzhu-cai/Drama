
def is_balanced(parentheses: str) -> bool:
    balance = 0
    for char in parentheses:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    
    # Check both concatenation orders
    if is_balanced(s1 + s2) or is_balanced(s2 + s1):
        return 'Yes'
    else:
        return 'No'

# Example test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
print(match_parens(['((', '))']))   # Output: 'No'
print(match_parens(['((', '())']))   # Output: 'Yes'
print(match_parens(['(())', '()']))  # Output: 'Yes'
print(match_parens(['(', ')']))      # Output: 'Yes'
print(match_parens(['(()', '())']))  # Output: 'Yes'
print(match_parens(['())', '(()']))  # Output: 'No'
