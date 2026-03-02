from records import *
print('Student Records Management System')

records = StudentRecords()
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

def menu_opt_validation(variable):
    while variable == '' or variable.isnumeric() is False:
        variable = input('Invalid input.\nEnter valid input:\n')
    while int(variable) < 1 or int(variable) > 5:
        variable = input('Value should be in the range (1-5):\n')
    return int(variable)

def print_menu(menu_options):
    for index, option in enumerate(menu_options, start = 1):
        print(f'{index}. {option}')

# Start of program
A = 0
while A == 0:
    menu = ['Add student(s) record', 'View student(s) record', 'Update student(s) record', 'Statistics', 'Exit']
    print_menu(menu)
    print('Menu can be accessed anytime by typing (menu)')
    options = input('Select an option (1-5): \n')
    options = menu_opt_validation(options)

    # Add Student(s)
    if options == 1:
        try:
            total = input('Enter number of students you wish to enter:\n')
            if total == 'menu':
                break
            total = int(total)
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
                A += 1
                break
            elif student == 'Menu':
                break
            # Receive score and validate input
            score = input(f'Enter {student} score:\n')
            score = score_validation(score)
            print(f'{student} scored {score}')

            # Store in dictionary
            records.add_student(student,score)
            counter += 1

    # View all records
    elif options == 2:
        if records.records != {}:
            for index, (key, values) in enumerate(records.records.items(), start = 1):
                print(f'{index}. {key} : {values}')
        else:
            print('No records have been entered')
    
    # Update a record
    elif options == 3:
        # proceed = ['yes', 'no']
        student_update = input('Enter name of student whose records you need to update\n Enter only existing students')
        student_update = student_update.strip().lower()
        student_update = string_validation(student_update)
        if student_update == 'menu':
            print_menu(menu)
        elif student_update == 'end':
            A += 1
            break
        # while student_update not in records.records:
        #    student_update = input('Invalid input, please enter a valid student name: \n')
        #    student_update = update.strip().lower()
        #    student_update = string_validation(update)
        # if student_update in records.records:
        #     if update == 'yes':
        #         update_student = input('Enter student name to be updated:\n')
        #         update_student = string_validation(update_student)
        #         if len(records.records) == 0:
        #             print('No record to update.')
        #         elif update_student in records.records:
        #             new_score = input(f'Enter {update_student} new score:\n')
        #             new_score = score_validation(new_score)
        #             records.add_student(update_student, new_score)
        #         elif update_student not in records.records:
        #             print(f'{update_student} not found in records.')
        #     else:
        #         print('No update performed.')
        records.update_student(student_update,score)

    # Statistics
    elif options == 4:              
        stats_opt = ['Number of students', 'Largest score', 'Smallest score', 'Average score', 'All statistics']
        print_menu(stats_opt)
        print('---------------------')
        if records.records != {}:
            stats_input = input('What statistics would you like to see??\n')
            stats_input = menu_opt_validation(stats_input)

            scores = records.records.values()
            score = list(scores)

            # Number of students
            if stats_input == 1:
                no_of_students = len(records.records)
                print(f'Number of students: {no_of_students}')
            elif stats_input == 2:
                # Max score
                max_score = max(score)
                for key, value in records.records.items():
                    if value == max_score:
                        high_std = key
                print(f'Highest score: {max_score} scored by {high_std}')
            elif stats_input == 3:
                # Min score
                min_score = min(score)
                print(f'Lowest score: {min_score}')
            elif stats_input == 4:
                # Average score
                avg_score = sum(score) / len(records.records)
                print(f'The average score is: {avg_score}')
            else:
                print(f'No available statistics')
        else:
            print('No records available for statistics.')
    elif options == 5:
        quit()
    else:
        print('Invalid option selected. Exiting program')
        quit()
