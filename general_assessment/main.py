import json
from collections import OrderedDict
import sys

from csv_parsing import data
from data_organization import get_total_average, get_course_info


students_list = data['students']
students_info = []
students_obj = {}


if len(sys.argv) != 6:
    print('Please input: courses, students, tests, and marks csv files, and output json file')
    sys.exit(0)
else:
    output = sys.argv[5]


for student in students_list:
    od = OrderedDict()
    student_id = student[0]
    student_name = student[1]

    od['id'] = student_id
    od['name'] = student_name
    od['totalAverage'] = get_total_average(student_id)
    od['courses'] = get_course_info(student_id)

    students_info.append(od)


students_obj['students'] = students_info


with open(output, 'w') as outfile:
    json.dump(students_obj, outfile, indent=2)