'''
Student information management
'''
from os import system
import csv

# ===========================
# Student Class
# ===========================
class Student:
    def __init__(self, idno, lastname, firstname, course, level):
        self.idno = idno
        self.lastname = lastname
        self.firstname = firstname
        self.course = course
        self.level = level


# ===========================
# Globals
# ===========================
filename: str = 'student.csv'
slist: list = []  # local data container, not persistent


# ===========================
# Display Menu
# ===========================
def displaymenu() -> None:
    system('cls')  # clear screen (works on Windows)
    print("\n" * 2)
    print(" STUDENT INFORMATION MANAGEMENT ".center(168, "="))
    print("1. Add Student".center(168))
    print("2. Find Student".center(168))
    print("3. Delete Student".center(168))
    print("4. Update Student".center(168))
    print("5. Display All Students".center(168))
    print("6. Save to File".center(168))
    print("7. Load from File".center(168))
    print("0. Exit".center(168))
    print("".center(168, "="))


# ===========================
# File Management
# ===========================
def load() -> None:
    global slist
    try:
        with open(filename, newline="", mode="r") as f:
            reader = csv.reader(f)
            slist = [Student(*row) for row in reader]
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing file found. Starting with empty list.")
    input("Press Enter to continue...")


def updater() -> None:
    with open(filename, newline="", mode="w") as f:
        writer = csv.writer(f)
        for s in slist:
            writer.writerow([s.idno, s.lastname, s.firstname, s.course, s.level])
    print("Data saved successfully.")
    input("Press Enter to continue...")


# ===========================
# Utility Functions
# ===========================
def addrecord(student: Student) -> bool:
    if findrecord(student.idno) is None:
        slist.append(student)
        return True
    return False


def findrecord(idno: str) -> Student:
    for s in slist:
        if s.idno == idno:
            return s
    return None


def deleterecord(idno: str) -> bool:
    s = findrecord(idno)
    if s:
        slist.remove(s)
        return True
    return False


def updaterecord(student: Student) -> bool:
    s = findrecord(student.idno)
    if s:
        s.lastname = student.lastname
        s.firstname = student.firstname
        s.course = student.course
        s.level = student.level
        return True
    return False


def displaylist() -> None:
    print("\n ================ STUDENT LIST ================ ".center(168))
    print("\n")
    if not slist:
        print("No records found.".center(168))
    else:
        for s in slist:
            print(f"{s.idno} | {s.lastname}, {s.firstname} | {s.course} | Level {s.level}")
    input("\nPress Enter to continue...")


# ===========================
# Input Validation Helpers
# ===========================
def input_id(prompt="ID Number: ") -> str:
    while True:
        val = input(prompt)
        if val.isdigit():
            return val
        else:
            print("ID must be numbers only. Try again.")


def input_text(prompt="Enter text: ") -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        else:
            print("This field cannot be empty. Try again.")


def input_level(prompt="Level: ") -> str:
    while True:
        val = input(prompt)
        if val.isdigit():
            return val
        else:
            print("Level must be numbers only. Try again.")


# ===========================
# Main Program
# ===========================
def main() -> None:
    option: str = ""
    while option != '0':
        displaymenu()
        option = input("Select option: ")

        match option:
            case '1':  # Add
                idno = input_id("ID Number: ")
                lastname = input_text("Last Name: ")
                firstname = input_text("First Name: ")
                course = input_text("Course: ")
                level = input_level("Level: ")

                student = Student(idno, lastname, firstname, course, level)
                if addrecord(student):
                    print("Student added successfully.")
                else:
                    print("Duplicate ID. Student not added.")
                input("Press Enter to continue...")

            case '2':  # Find
                idno = input_id("Enter ID to find: ")
                s = findrecord(idno)
                if s:
                    print(f"Found: {s.idno} - {s.lastname}, {s.firstname} ({s.course}, Level {s.level})")
                else:
                    print("Student not found.")
                input("Press Enter to continue...")

            case '3':  # Delete
                idno = input_id("Enter ID to delete: ")
                if deleterecord(idno):
                    print("Record deleted.")
                else:
                    print("Student not found.")
                input("Press Enter to continue...")

            case '4':  # Update
                idno = input_id("Enter ID to update: ")
                lastname = input_text("New Last Name: ")
                firstname = input_text("New First Name: ")
                course = input_text("New Course: ")
                level = input_level("New Level: ")

                student = Student(idno, lastname, firstname, course, level)
                if updaterecord(student):
                    print("Record updated successfully.")
                else:
                    print("Student not found.")
                input("Press Enter to continue...")

            case '5':  # Display
                displaylist()

            case '6':  # Save
                updater()

            case '7':  # Load
                load()

            case '0':  # Exit
                print("Exiting program...")
                break

            case _:  # Invalid
                print("Invalid option.")
                input("Press Enter to continue...")


# ===========================
# Launcher
# ===========================
if __name__ == "__main__":
    main()
