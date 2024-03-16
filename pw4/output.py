def display_menu():
    print("\nMenu:")
    print("1. Input Students")
    print("2. Input Courses")
    print("3. Input Student Marks")
    print("4. List Students")
    print("5. List Courses")
    print("6. Show Student Marks")
    print("7. Calculate GPA")
    print("0. Exit")

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"ID: {course.course_id}, Name: {course.name}, Credits: {course.credits}")

def show_student_marks(marks):
    student_id = input("Enter student ID to show marks: ")
    course_id = input("Enter course ID to show marks: ")

    # Find the marks for the specified student and course
    for mark in marks:
        if mark.student_id == student_id and mark.course_id == course_id:
            print(f"Marks for student {student_id} in course {course_id}: {(mark.marks)}")
            return

    print(f"No marks found for student {student_id} in course {course_id}.")

def cal_gpa(students, marks):
    for student in students:
        student_marks = []
        for mark in marks:
            if mark.student_id == student.student_id:
                student_marks.append(mark.marks)
        if student_marks:
            gpa = sum(student_marks) / len(student_marks)
            print(f"GPA of student {student.student_id} is: {gpa}")
        else:
            print(f"No marks found for student {student.student_id}")
