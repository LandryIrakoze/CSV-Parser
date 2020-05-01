import csv
import sys
from os import path


courses = sys.argv[1]
students = sys.argv[2]
tests = sys.argv[3]
marks = sys.argv[4]


# checks if files are valid:
def validate_files(file_name):
    if path.exists(file_name):
        file_extension = file_name.split('.')[1]
        
        if file_extension != 'csv':
            print('please enter valid csv files')
            sys.exit(0)
    else:
        print('file does not exist')
        sys.exit(0)


# outputs 2d array from csv data
def parse_csv(file_name):
    output_list = []
    
    with open(file_name) as file:
        for row in file:
            line = row.split(',')
            output_list.append(line)

    return output_list


# outputs array with newline flags removed and string ints converted to ints
def clean(arr):
    cleaned_arr = arr[:]
    for i, item in enumerate(arr):
        for j, elem in enumerate(item):
            stripped = elem.strip("\n")
            if stripped.isnumeric():
                cleaned_arr[i][j] = int(stripped)
            else:
                cleaned_arr[i][j] = stripped

    return cleaned_arr


validate_files(courses)
validate_files(students)
validate_files(tests)
validate_files(marks)


# cleans and parses csv data
marks = clean(parse_csv(marks)[1:])
students = clean(parse_csv(students)[1:])
tests = clean(parse_csv(tests)[1:])
courses = clean(parse_csv(courses)[1:])


# populates data object with parsed and cleaned list of data from csv file
data = {}
data['courses'] = courses
data['students'] = students
data['tests'] = tests
data['marks'] = marks