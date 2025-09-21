'''
Student information management
'''
from os import system

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
slist: list = []  # local data container, not persistent


# ===========================
# Display Menu
# ===========================
def displaymenu() -> None:
    system('cls')  # clear screen (works on Windows)
    print("\n" * 2)
    print(" STUDENT INFORMATION MANAGEMENT ".center(168, "="))
    print("1. Add Student".center(168))
    print("2. Find Student".center(170))
    print("3. Delete Student".center(171))
    print("4. Update Student".center(171))
    print("5. Display All Students".center(178))
    print("0. Exit".center(161))
    print("".center(170, "="))


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
    print("\n ================ STUDENT LIST ================ ")
    print("\n")
    if not slist:
        print("No records found.".center(168))
    else:
        for s in slist:
            print(f"{s.idno} | {s.lastname}, {s.firstname} | {s.course} | Level {s.level}")
    input("\nPress Enter to continue...".center(165))


# ===========================
# Input Validation Helpers
# ===========================
def input_id(prompt="ID Number: ") -> str:
    while True:
        val = input(prompt)
        if val.isdigit():
            return val
        else:
            print("ID must be numbers only. Try again.".center(190))


def input_text(prompt="Enter text: ") -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        else:
            print("This field cannot be empty. Try again.".center(165))


def input_level(prompt="Level: ") -> str:
    while True:
        val = input(prompt)
        if val.isdigit():
            return val
        else:
            print("Level must be numbers only. Try again.".center(190))


# ===========================
# Main Program
# ===========================
def main() -> None:
    option: str = ""
    while option != '0':
        displaymenu()
        option = input("Select option: ".center(170))

        match option:
            case '1':  # Add 
                idno = input_id("ID Number: ".center(165))
                lastname = input_text("Last Name: ".center(165))
                firstname = input_text("First Name: ".center(165))
                course = input_text("Course: ".center(161))
                level = input_level("Level: ".center(161))

                student = Student(idno, lastname, firstname, course, level)
                if addrecord(student):
                    print("Student added successfully.".center(165))
                else:
                    print("Duplicate ID. Student not added.".center(165))
                input("Press Enter to continue...".center(165))

            case '2':  # Find
                idno = input_id("Enter ID to find: ".center(165))
                s = findrecord(idno)
                if s:
                    print(f"Found: {s.idno} - {s.lastname}, {s.firstname} ({s.course}, Level {s.level})")
                else:
                    print("Student not found.".center(165))
                input("Press Enter to continue...".center(165))

            case '3':  # Delete
                idno = input_id("Enter ID to delete: ".center(165))
                if deleterecord(idno):
                    print("Record deleted.".center(165))
                else:
                    print("Student not found.".center(165))
                input("Press Enter to continue...".center(165))

            case '4':  # Update
                idno = input_id("Enter ID to update: ".center(168)) 
                lastname = input_text("New Last Name: ".center(168))
                firstname = input_text("New First Name: ".center(168))
                course = input_text("New Course: ".center(168))
                level = input_level("New Level: ".center(168))

                student = Student(idno, lastname, firstname, course, level)
                if updaterecord(student):
                    print("Record updated successfully.".center(165))
                else:
                    print("Student not found.".center(165))
                input("Press Enter to continue...".center(165))

            case '5':  # Display
                displaylist()

            case '0':  # Exit
                print("Exiting program...".center(165))
                break

            case _:  # Invalid
                print("Invalid option.".center(165))
                input("Press Enter to continue...".center(165))


# ===========================
# Launcher
# ===========================
if __name__ == "__main__":
    main()
