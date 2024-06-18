import re
import os
# Project 4:  registration system
#Rebekah shi
#3/24/24

class_name = ''
def create_new_class():
    #explain the prompt
    print('Follow the following instructions. Class sizes are limited')
    class_name = input('Input the class name: ')
    class_file_name = input('Input the file name for this class: e.g class.txt ')
    class_file = open(class_file_name, 'w')
    #write some beginning lines that explain the class structure when open file
    line1, line2 = 'Class name: ' + class_name + '\n', 'Class size: 24' + '\n'
    control = 'RebekahShi'
    class_file.write(line1)
    class_file.write(line2)
    class_file.write(control)
    class_file.close()

def update_class_list():
    #update the class lsit by calling the enroll and unenroll class as seen below
    open_class_file = input('Enter file name: ')
    open_class_file = open_class_file.strip()
    class_list_file = open(open_class_file)
    options = input('1 for adding student \n 2 for removing student')
    if int(options) == 1:
        enroll_class()
    if int(options) == 2:
        unenroll_class()

def delete_class():
    #check to see if the file exists, and then delete
    class_file_name = input('Enter the full file name to delete: ')
    if os.path.exists(class_file_name):
        os.remove(class_file_name)
    else:
        print('File does not exist')

def print_class_roster():
    #print the roster line by line
    file = input('Enter the class name to print the list of students: ')
    file = file.strip() + '.txt'
    class_file_name = open(file)
    for line in class_file_name:
        print(line + '\n')
def enroll_class():
    #try to open file and state class file does not exist if not
    try:
        file = input('Enter the class name you wish to enroll')
        name_of_class = file.strip()
        file = file.strip() + '.txt'
        fhand = open(file)
    except:
        print('Sorry, class does not exist')
        exit()
    #open the file and transfer to list, close the file , if the list is at capacity, state class is full. Else, have student enter their full name,
    #trum any whitespae, and put in list are a name by append to the end and write to file.
    fhand = open(file)
    class_file_name = fhand.read()
    class_list = class_file_name.split()
    fhand.close()
    if len(class_list) == 30:
        print('This class is full.')
    else:
        student_name = input('Enter Full name: ')
        student_name = student_name.replace(' ', '')
        class_list.append(student_name)
        class_list = '\n'.join(class_list)
        rewrite = open(file, 'w')
        rewrite.write(class_list)
        rewrite.close()
        student_classes_l = []
        student_classes_l.append(file)

        #open student's files and read contents, make into list, append newly enrolled class and write to file. then close

        update_student_class = open(student_name + '.txt', 'w+')
        class_student = update_student_class.read()
        students_classes = class_student.split()
        students_classes.append(name_of_class)
        students_classes_str = '\n'.join(students_classes)
        update_student_class.write(students_classes_str)
        #update_student_class.close()
        update_student_class.close()
        # updated_student_class = open(student_name + '.txt', 'w')
        # updated_student_class.write(students_classes_str)
        # updated_student_class.close()





def unenroll_class():
    # try to open file and state class file does not exist if not
    # open the file and transfer to list, close the file , have student enter their full name,
    # trum any whitespace, and the list. write the new list to the file and close
    try:
        file = input('Enter the class name you wish to unenroll from')
        name_of_class = file.strip()
        file = file.strip() + '.txt'
        fhand = open(file)
    except:
        print('Sorry, class does not exist')
        exit()
    student_name = input('Enter Full name: ')
    student_name = student_name.replace(' ', '')
    try:
        remove_update = open(file)
        class_file_name = remove_update.read()
        class_list = class_file_name.split()
        remove_update.close()
        rewrite = class_list
        rewrite.remove(student_name)
        rewrite = ' '.join(rewrite)
        remove_update = open(file, 'w+')
        remove_update.write(rewrite)
        remove_update.close()
        # open student's files and read contents, make into list, append newly enrolled class and write to file. then close
        update_student_class = open(student_name + '.txt', 'w+')
        class_student = update_student_class.read()
        students_classes = class_student.split()
        students_classes.remove(name_of_class)
        students_classes_str = '\n'.join(students_classes)
        update_student_class.write(students_classes_str)
        update_student_class.close()
    except:
        print('This student is not enrolled in this class')



def view_classes():
    student_name_view_class = input('Please enter name to see your list of classes: ')
    student_name_view_class = student_name_view_class.replace(' ', '')
    student_file = student_name_view_class + '.txt'
    try:
        student_file = open(student_file)
    except:
        print('You have no classes signed up. Sign up!')
        student_file = open(student_file, 'w+')
    student_class_file = student_file.read()
    student_class_list = student_class_file.split()
    student_file.close()
    print('You are signed up for the following classes: ')
    for c in student_class_list:
        print(c + '\n')



while True:
    # Ask user for mode
    mode = input('Please select a mode:\n 1 for Admin \n 2 for Student \n 3 to Exit')
    # if the mode is admin display the menu for the options, call the functions as needed
    if mode == '1':
        option = input(
            'Please select an option: \n 1 for Create New Class \n 2 for Delete a Class \n 3 for Update a Class file \n 4 for Print a class roster\n 5 to exit program')
        if int(option) == 1:
            create_new_class()
        if int(option) == 2:
            delete_class()
        if int(option) == 3:
            view_classes()
            update_class_list()
        if int(option) == 4:
            print_class_roster()
        if int(option) == 5:
            print('Thank you for using this program.')
            break
    # if the mode is student, display the menu for the options, call the functions as needed
    if mode == '2':
        option = input('Please select an option: \n 1 for Enroll class \n 2 for Unenroll class')
        print('Please enter you name: ')
        view_classes()
        # implement student mode
        if int(option) == 1:
            enroll_class()
        if int(option) == 2:
            unenroll_class()
    if mode == '3':
        print('Thank you for using this program.')
        break

