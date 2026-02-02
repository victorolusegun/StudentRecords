print('Welcome')

# Functions
def string_validation(variable):
    while variable == '' or variable.isnumeric() is True:
        variable = input('Invalid input.\nEnter valid input:\n')
    return variable

def score_validation(variable):
    while variable == '' or variable.isnumeric() is False:
        variable = input('Invalid input.\nEnter valid input:\n')
    while int(variable) < 0 or int(variable) > 100:
        variable = input('Value should be in the range 0-100:\n')
    return int(variable)

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
    score = score_validation(score)
    print(f'{student} scored {score}')

    # Store in dictionary
    records[student] = score
    counter += 1

# View all records
for index, (key, values) in enumerate(records.items(), start = 1):
    print(f'{index}. {key} : {values}')

# Update a record
update = input('Do you want to update any record? (yes/no):\n')
update = update.strip().lower()
update = string_validation(update)
if update == 'yes':
    update_student = input('Enter student name to be updated:\n')
    update_student = string_validation(update_student)
    if len(records) == 0:
        print('No record to update.')
    elif update_student in records:
        new_score = input(f'Enter {update_student} new score:\n')
        new_score = score_validation(new_score)
        records[update_student] = new_score
    elif update_student not in records:
        print(f'{update_student} not found in records.')
else:
    print('No update performed.')
        
# Statistics. Extract scores from dictionary
stats_opt = ['Number of students', 'Largest score', 'Smallest score', 'Average score']
for index, options in enumerate(stats_opt, start = 1):
    print(f'{index}. {options}')
print('---------------------')
if records != {}:
    stats_input = input('What statistics would you like to see??\n')
    stats_input = score_validation(stats_input)

    scores = records.values()
    score = list(scores)

    # Number of students
    if stats_input == 1:
        no_of_students = len(records)
        print(f'Number of students: {no_of_students}')
    elif stats_input == 2:
        # Max score
        max_score = max(score)
        for key, value in records.items():
            if value == max_score:
                high_std = key
        print(f'Highest score: {max_score} scored by {high_std}')
    elif stats_input == 3:
        # Min score
        min_score = min(score)
        print(f'Lowest score: {min_score}')
    elif stats_input == 4:
        # Average score
        avg_score = sum(score) / len(records)
        print(f'The average score is: {avg_score}')
    else:
        print(f'No available statistics')
else:
    print('No records available for statistics.')
