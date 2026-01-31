print('Welcome')

# Functions
def string_validation(variable):
    while variable == '' or variable.isnumeric() is True:
        variable = input('Invalid input.\nEnter valid input:\n')
    return variable

def int_validation(variable):
    while variable == '' or variable.isnumeric() is False:
        variable = input('Invalid input.\nEnter valid input:\n')
    variable = int(variable)
    return variable

records = {}

try:
    total = int(input('Enter number of students you wish to enter:\n'))
except ValueError:
    print('Invalid input, defaulting to 1 student.')
    total = 1
counter = 0
while counter < total:
    # Collect student name and validate input
    student = input('Enter student name (Enter end to stop):\n')
    student = string_validation(student)
    student = student.strip().capitalize()
    if student == 'End':
        break

    # Receive score and validate input
    score = input(f'Enter {student} score:\n')
    score = int_validation(score)
    while score< 0 or score > 100:
        score = input('Value should be in the range 0-100:\n')
        score = int_validation(score)
    print(f'{student} scored {score}')

    # Store in dictionary
    records[student] = score
    counter += 1

for index, (key, values) in enumerate(records.items()):
    print(f'{index+1}. {key} scored {values}')