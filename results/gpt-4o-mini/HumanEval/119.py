
def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    
    # Count open and close parentheses in both strings
    open1 = s1.count('(')
    close1 = s1.count(')')
    open2 = s2.count('(')
    close2 = s2.count(')')
    
    # Check the first concatenation order: s1 + s2
    if open1 + open2 >= close1 + close2 and open1 >= close2:
        return 'Yes'
    
    # Check the second concatenation order: s2 + s1
    if open2 + open1 >= close2 + close1 and open2 >= close1:
        return 'Yes'
    
    return 'No'

# Example usage:
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
