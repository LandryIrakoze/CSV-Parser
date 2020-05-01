from collections import OrderedDict
from csv_parsing import data


def get_student_tests(student_id):
    student_test_list = filter(lambda x: x[1] == student_id, data['marks'])
    return list(student_test_list)


def get_course_weights(course_id):
    course_scores = filter(lambda x: x[1] == course_id, data['tests'])
    return list(course_scores)


def get_averages(student_id):
    student_tests = get_student_tests(student_id)

    weighted = {}
    for i in range(len(student_tests)):
        test_id = student_tests[i][0]

        if test_id != None:
            student_mark = student_tests[i][2]
            weight = data['tests'][test_id-1][2]
            course = data['tests'][test_id-1][1]
            final_score = student_mark*weight*.1

            if course not in weighted:
                weighted[course] = final_score
            else:
                weighted[course] = weighted[course] + final_score

    for item in weighted:
        weighted[item] = round(weighted[item]*.1,1)

    return weighted


def get_total_average(student_id):
    averages = get_averages(student_id).values()
    return round(sum(averages)/len(averages),2)


def get_course_info(student_id):
    courses = get_averages(student_id)
    course_info = []

    for item in courses:
        od = OrderedDict()
        od["id"] = item
        od["name"] = data['courses'][item-1][1]
        od["teacher"] = data['courses'][item-1][2]
        od["courseAverage"] = courses[item]
        course_info.append(od)
    return course_info