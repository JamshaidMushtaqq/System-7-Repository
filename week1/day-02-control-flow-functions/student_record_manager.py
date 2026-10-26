import json
import os

FILE_NAME = "student_records.json"

def load_student_records():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Could not read student records. Starting with an empty record.")
    return []
def save_student_records(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student_record(students):
    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()
    marks = input("Enter marks: ").strip()

    if not name or not roll_number:
        print("Name and roll number cannot be empty.")
        return
    if any(s["roll_number"] == roll_number for s in students):
        print("A student with this roll number already exists.")
        return

    try:
        marks = float(marks)
        if not 0 <= marks <= 100:
            print("Marks should be between 0 and 100.")
            return
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return

    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks
    }

    students.append(student)
    save_student_records(students)
    print("Student record added successfully.")

def view_students(students):
    if not students:
        print("No student records found.")
        return
    print("\n---------Student Records:---------")
    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Marks:", student["marks"])
        print("-------------------------------")

def main():
    students = load_student_records()
    while True:
        print("\n========== Student Record Manager ==========")
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student_record(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
        
