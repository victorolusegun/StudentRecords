print('Welcome')

# Functions
def string_validation(variable):
    while variable == '' or variable.isnumeric() is True:
        variable = input('Invalid input.\nEnter valid input:\n')
    return variable

def int_validation(variable):
    while variable == '' or variable.isnumeric() is False:
        variable = input('Invalid input.\nEnter valid input:\n')
    return variable

records = {}

try:
    total = int(input('Enter number of students you wish to enter:\n'))
except ValueError:
    total = 1
counter = 0
while counter < total:
    # Collect student name and validate input
    student = input('Enter student name (Enter exit to stop):\n')
    student = string_validation(student)
    student = student.strip().capitalize()
    if student == 'Exit':
        break
    
    # Receive score and validate input
    score = input(f'Enter {student} score:\n')
    score = int_validation(score)
    print(f'{student} scored {score}')

    # Store in dictionary
    records[student] = score
    counter += 1