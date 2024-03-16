from datetime import datetime
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

students = []
courses = []
marks = []
gpa = []

def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        while True:
            dob = input("Enter student Date of Birth(DD/MM/YYYY): ")
            if check_dob_format(dob):
                break
            else:
                print("Please enter the correct format")

        student = Student(student_id, name, dob)
        students.append(student)


def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_credits = int(input("Enter course credits: "))
        course = Course(course_id, course_name, course_credits)
        courses.append(course)

def input_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID to input marks: ")
    marks_value = float(input(f"Enter marks for course id: {course_id} for student {student_id}: "))
    mark = Mark(student_id, course_id, marks_value)
    marks.append(mark)

def check_dob_format(dob):
    try:
        date_format = ['%d/%m/%Y']
        for format in date_format:
            datetime.strptime(dob, format)
        return True
    except ValueError:
        print("Incorrect data format, should be DD/MM/YYYY")
        return False