from math import floor
#import numpy as np
from datetime import datetime

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class Mark:
    def __init__(self, student_id, course_id, marks):
        self.student_id = student_id
        self.course_id = course_id
        self.marks = marks

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def display_menu(self):
        print("\nMenu:")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Student Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Student Marks")
        print("0. Exit")

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            while True:
                dob = input("Enter student Date of Birth(DD/MM/YYYY): ")
                if self.check_dob_format(dob):
                    break
                else:
                    print("Please enter the correct format")

            student = Student(student_id, name, dob)
            self.students.append(student)

    def check_dob_format(self, dob):
        try:
            date_format = ['%d/%m/%Y']
            for format in date_format:
                datetime.strptime(dob, format)
            return True
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY")
            return False

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID to input marks: ")
        #round up the mark
        marks_value = floor(float(input(f"Enter marks for {course_id} for student {student_id}: ")))
        mark = Mark(student_id, course_id, marks_value)
        self.marks.append(mark)

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def list_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def show_student_marks(self):
        student_id = input("Enter student ID to show marks: ")
        course_id = input("Enter course ID to show marks: ")

        # Find the marks for the specified student and course
        for mark in self.marks:
            if mark.student_id == student_id and mark.course_id == course_id:
                print(f"Marks for student {student_id} in course {course_id}: {mark.marks}")
                return

        print(f"No marks found for student {student_id} in course {course_id}.")

if __name__ == "__main__":
    system = StudentManagementSystem()

    while True:
        system.display_menu()
        choice = input("Enter your choice (0-6): ")

        if choice == "1":
            system.input_students()
        elif choice == "2":
            system.input_courses()
        elif choice == "3":
            system.input_student_marks()
        elif choice == "4":
            system.list_students()
        elif choice == "5":
            system.list_courses()
        elif choice == "6":
            system.show_student_marks()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

