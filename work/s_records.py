from records import *
print('Student Records Management System')

records = StudentRecords()
# Functions
def string_validation(variable):
    while variable == '' or variable.isnumeric() is True:
        variable = input('Invalid input.\nEnter valid input:\n')
    variable = variable.strip().capitalize()
    return variable

def score_validation(variable):
    while variable == '' or variable.isnumeric() is False:
        variable = input('Invalid input.\nEnter valid input:\n')
    while int(variable) < 0 or int(variable) > 100:
        variable = input('Value should be in the range 0-100:\n')
    return int(variable)

def menu_opt_validation(variable):
    while variable == '' or variable.isnumeric() is False:
        variable = input('Invalid input (Numbers only).\nEnter valid input:\n')
    while int(variable) < 1 or int(variable) > 5:
        variable = input('Value should be in the range (1-5):\n')
    return int(variable)

def print_menu(menu_options):
    for index, option in enumerate(menu_options, start = 1):
        print(f'{index}. {option}')

def exit_program():
    print('----------------------')
    print('Exiting program...')
    quit('Program ended.\n----------------------')

# START PROGRAM
while True:
    while True:
        menu = ['Add student(s) record', 'View student(s) record', 'Update student(s) record', 'Statistics', 'Exit']
        print_menu(menu)
        print('NB: MENU CAN BE ACCESSED ANYTIME BY TYPING "menu" \nPROGRAM CAN BE EXITED ANYTIME BY TYPING "end" OR "exit".')
        options = input('Select an option (1-5)\n')
        options = menu_opt_validation(options)

        # Add Student(s)
        if options == 1:
            # Get total number of student user wants to add or use default
            try:
                total = input('Enter number of students you wish to enter:\n')
                if total == 'menu':
                    print('---------------------')
                    break
                elif total == 'exit' or total == 'end':
                   exit_program()
                total = int(total)
            except ValueError:
                print('Invalid input, defaulting to 1 student.')
                total = 1
            counter = 0
            while counter < total:
                # Collect student name and validate input
                student = input('Enter student name (Enter end/exit to quit program):\n')
                student = string_validation(student)
                if student == 'Menu':
                    break
                elif student == 'End' or student == 'Exit':
                    exit_program()
                # Receive score and validate input
                score = input(f'Enter {student} score:\n')
                score = score_validation(score)
                print(f'{student} scored {score}')

                # Store in dictionary
                records.add_student(student,score)
                counter += 1

        # View all records
        elif options == 2:
            records.view_student()
            print('---------------------')
            choices = ['Yes', 'No']
            proceed = input('Do you want to return to the menu? (yes/no)\n')
            proceed = string_validation(proceed)
            while proceed not in choices:
                proceed = input('Invalid input, please enter (yes/no)\n')
            if proceed == 'Yes' or proceed == 'Menu':
                break
            elif proceed == 'No' or proceed == 'End' or proceed == 'Exit':
                exit_program()
        
        # Update a record
        elif options == 3:
            if len(records.records) == 0:
                print('---------------------')
                print('No records to update')
                print('---------------------')
            else:
                student_update = input('Enter name of student whose records you need to update\nEnter only existing student\n')
                student_update = string_validation(student_update)
                if student_update == 'menu':
                    print('---------------------')
                    break
                elif student_update == 'end' or student_update == 'exit':
                    exit_program()
                while student_update not in records.records:
                    student_update = input('Invalid input, please enter a valid student name: \n')
                    student_update = string_validation(student_update)
                if student_update in records.records:
                    new_score = input(f'Enter {student_update} new score:\n')
                    new_score = score_validation(new_score)
                    records.update_student(student_update,new_score)
                elif student_update not in records.records:
                    records.update_student(student_update, new_score)
                else:
                    print('No update performed.')
                

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
            print('\n----------------------')
            print('Exiting program...')
            quit('Program ended.\n----------------------')
        else:
            print('Invalid option selected. Exiting program')
            quit()
print('Program ended.')