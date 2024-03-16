from input import input_students, input_courses, input_student_marks, students, courses, marks
from output import display_menu, list_students, list_courses, show_student_marks, cal_gpa

if __name__ == "__main__":
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
            list_students(students)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            show_student_marks(marks)
        elif choice == "7":
            cal_gpa(students, marks)
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 7.")
