print('Welcome')

# def val_input(student):
    
records = {}

student = input('Enter student name: \n')
while student == '' or student.isnumeric() is True:
    student = input('Name can not be empty or numeric. Enter valid name: \n')
student = student.capitalize()
print(f'Hello, {student}!')