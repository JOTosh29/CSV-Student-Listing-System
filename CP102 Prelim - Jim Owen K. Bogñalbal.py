import csv
import os
import shutil

students = []

# Path to the CSV file
csv_file_path = r'C:\Users\Jim Owen\Downloads\CSV\students.csv'

# Load students from the provided CSV file or create a new file if it doesn't exist
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        students.extend(list(reader))
else:
    print(f"CSV file '{csv_file_path}' not found. Creating a new file.")

# Function to save students to the CSV file
def save_students_to_csv(file_path):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'student_id', 'gender', 'course']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    print(f"Student data saved to {file_path}.")

# Function to create a backup of the CSV file
def create_backup(file_path):
    backup_path = file_path.replace('.csv', '_backup.csv')
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")

# Function to add a new student to the list
def add_student():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        else:
            print("Please enter a valid student name.")

    while True:
        student_id = input("Enter student ID: ").strip()
        if student_id:
            break
        else:
            print("Please enter a valid student ID.")

    while True:
        gender = input("Enter student gender (M or Male, F or Female): ").strip().upper()
        if gender in ['M', 'MALE', 'F', 'FEMALE']:
            break
        else:
            print("Please enter a valid gender (M for Male, F for Female).")

    course = input("Enter student course: ").strip()

    students.append({"name": name, "student_id": student_id, "gender": gender, "course": course})
    print(f"{name} added to the list of students.")

# Function to remove a student from the list
def remove_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"{student['name']} removed from the list of students.")
            return
    print(f"No student with the name {name} found in the list.")

# Function to search for students by name
def search_by_name(name):
    found_students = []
    for student in students:
        if name.lower() in student["name"].lower():
            found_students.append(student)
    return found_students if found_students else None

# Function to search for a student by ID
def search_by_id(student_id):
    for student in students:
        if student["student_id"].lower() == student_id.lower():
            return student
    return None

# Function to display all students
def display_students():
    print("Students in the list:")
    for student in students:
        print(
            f"Name: {student['name']}, ID: {student['student_id']}, Gender: {student['gender']}, Course: {student['course']}")

# Function to display profile of a single student
def display_student_profile(student, first_student=False):
    if not first_student:
        print()
    print(
        f"Name: {student['name']}\nID: {student['student_id']}\nGender: {student['gender']}\nCourse: {student['course']}")

# Function to exit the program
def exit_program():
    save_students_to_csv(csv_file_path)
    create_backup(csv_file_path)
    print("Exiting the program. Thank you!")
    exit()

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student by Name")
    print("4. Search Student by ID")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1" or choice.lower() == "add":
        add_student()

    elif choice == "2" or choice.lower() == "remove":
        remove_name = input("Enter student name to remove: ")
        remove_student(remove_name)

    elif choice == "3" or choice.lower() == "search name":
        search_name = input("Enter student name to search: ")
        found_students = search_by_name(search_name)
        if found_students:
            print("Students found! Profiles:")
            for idx, found_student in enumerate(found_students):
                display_student_profile(found_student, idx == 0)
        else:
            print(f"No students found with the name {search_name}.")

    elif choice == "4" or choice.lower() == "search id":
        search_id = input("Enter student ID to search: ")
        found_student = search_by_id(search_id)
        if found_student:
            print("Student found! Profile:")
            display_student_profile(found_student)
        else:
            print(f"No student found with the ID {search_id}.")

    elif choice == "5" or choice.lower() == "display":
        if students:
            display_students()
        else:
            print("No students in the list.")

    elif choice == "6" or choice.lower() == "exit":
        exit_program()

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
