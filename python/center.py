from os import system
from studentlist import StudentList
from student import Student

slist = StudentList(10)

def displaymenu() -> None:
    system('cls')
    for i in range(1,5):print(" "*73)    
    print("       MAIN MENU        ".center(73, " "))
    print(" -----------------------".center(73, " "))
    print(" 1. ADD STUDENT         ".center(73, " "))
    print(" 2. FIND STUDENT        ".center(73, " "))
    print(" 3. DELETE STUDENT      ".center(73, " "))
    print(" 4. UPDATE STUDENT      ".center(73, " "))
    print(" 5. DISPLAY ALL STUDENT ".center(73, " "))
    print(" 0. QUIT/END            ".center(73, " "))
    print(" -----------------------".center(73, " "))

def get_valid_input(prompt: str, type_: str) -> str:
    while True:
        value = input(prompt)
        if type_ == "num" and value.isdigit():
            return value
        elif type_ == "str" and value.isalpha():
            return value
        else:
            print("Invalid input. Try again!")

def addstudent() -> None:
    system('cls')
    print("Add Student".center(73))
    print("----------------------".center(73))
    print(" "*25,end="")
    idno = get_valid_input("IDNO      : ", "num")
    print(" "*25,end="")
    lastname = get_valid_input("LASTNAME  : ", "str")
    print(" "*25,end="")
    firstname = get_valid_input("FIRSTNAME : ", "str")
    print(" "*25,end="")
    course = get_valid_input("COURSE    : ", "str")
    print(" "*25,end="")
    level = get_valid_input("LEVEL     : ", "num")
    print(" "*25,end="")
    if slist.addstudent(Student(idno, lastname, firstname, course, level)):
        print("Student added successfully!")
    else:
        print("Student list is full!")

def findstudent() -> None:
    system('cls')
    idno = get_valid_input("Enter IDNO to find: ", "num")
    student = slist.findstudent(idno)
    if student:
        print(f"Found: {student.getidno()} {student.getlastname()} {student.getfirstname()} {student.getcourse()} {student.getlevel()}")
    else:
        print("Student not found!")

def deletestudent() -> None:
    system('cls')
    idno = get_valid_input("Enter IDNO to delete: ", "num")
    if slist.deletestudent(idno):
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def updatestudent() -> None:
    system('cls')
    idno = get_valid_input("Enter IDNO to update: ", "num")
    student = slist.findstudent(idno)
    if student:
        print("Enter new data:")
        lastname = get_valid_input("LASTNAME  : ", "str")
        firstname = get_valid_input("FIRSTNAME : ", "str")
        course = get_valid_input("COURSE    : ", "str")
        level = get_valid_input("LEVEL     : ", "num")
        slist.updatestudent(Student(idno, lastname, firstname, course, level))
        print("Student updated successfully!")
    else:
        print("Student not found!")

def displayall() -> None:
    system('cls')
    slist.showlist()

def main() -> None:
    option = ""
    while option != "0":
        displaymenu()
        print(" "*25,end="")
        option = input(" Enter Option(0..5): ")
        match option:
            case "1": addstudent()
            case "2": findstudent()
            case "3": deletestudent()
            case "4": updatestudent()
            case "5": displayall()
            case "0": print("Program Ended".center(73))
            case _: print("Invalid Option".center(73))
        print(" "*25,end="")
        input("Press any key to continue...")

if __name__ == "__main__":
    main()
