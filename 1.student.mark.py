students = []
courses = []
marks = []

def display_menu():
    print("\nMenu:")
    print("1. Input Students")
    print("2. Input Courses")
    print("3. Input Student Marks")
    print("4. List Students")
    print("5. List Courses")
    print("6. Show Student Marks")
    print("0. Exit")

def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth: ")
        students.append({"id": student_id, "name": name, "dob": dob})

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({"id": course_id, "name": course_name})

def input_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID to input marks: ")
    marks_value = float(input(f"Enter marks for {course_id} for student {student_id}: "))
    marks.append({"student_id": student_id, "course_id": course_id, "marks": marks_value})

# Listing functions
def list_students():
    print("List of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses():
    print("List of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_student_marks():
    student_id = input("Enter student ID to show marks: ")
    course_id = input("Enter course ID to show marks: ")
    
    # Find the marks for the specified student and course
    for mark in marks:
        if mark["student_id"] == student_id and mark["course_id"] == course_id:
            print(f"Marks for student {student_id} in course {course_id}: {mark['marks']}")
            return
    
    print(f"No marks found for student {student_id} in course {course_id}.")

while True:
    display_menu()
    choice = input("Enter your choice (0-6): ")

    if choice == "1":
        input_students()
    elif choice == "2":
        input_courses()
    elif choice == "3":
        input_student_marks()
    elif choice == "4":
        list_students()
    elif choice == "5":
        list_courses()
    elif choice == "6":
        show_student_marks()
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 6.")
