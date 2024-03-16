from datetime import datetime
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import zipfile
#changes
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
        with open("pw5/students.txt", "a") as file:
            file.write(f"Student ID: {student_id}, Name: {name}, Date of Birth: {dob}\n")
        student = Student(student_id, name, dob)
        students.append(student)


def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_credits = int(input("Enter course credits: "))
        with open("pw5/courses.txt", "a") as file:
            file.write(f"Course ID: {course_id}, Course Name: {course_name}, Course Credits: {course_credits}\n")
        course = Course(course_id, course_name, course_credits)
        courses.append(course)

def input_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID to input marks: ")
    marks_value = float(input(f"Enter marks for course id: {course_id} for student {student_id}: "))
    with open("pw5/marks.txt", "a") as file:
        file.write(f"Student ID: {student_id}, Course ID: {course_id}, Marks: {marks_value}\n")
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
def compress_files():
    with zipfile.ZipFile("pw5/student.dat", "w") as zipf:
        zipf.write("pw5/students.txt")
        zipf.write("pw5/courses.txt")
        zipf.write("pw5/marks.txt")