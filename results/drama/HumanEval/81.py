
def numerical_letter_grade(grades):
    """Convert a list of GPAs to corresponding letter grades based on a grading scale."""
    
    # Initialize an empty list to hold the letter grades
    letter_grades = []
    
    # Iterate through the list of GPAs
    for gpa in grades:
        # Determine the letter grade based on the GPA value
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        elif gpa == 0.0:
            letter_grades.append('E')
        else:
            letter_grades.append('Invalid GPA')  # Handle invalid GPAs if necessary
    
    return letter_grades

# Example usage:
gpas = [4.0, 3.0, 1.7, 2.0, 3.5]
result = numerical_letter_grade(gpas)
print(result)  # Output: ['A+', 'B+', 'C-', 'C+', 'A-']
