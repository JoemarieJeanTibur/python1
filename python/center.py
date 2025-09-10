'''
	centering the menu'
'''
from os import system
from studentlist import StudentList
from student import Student

slist = StudentList(10)

def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(" "*73)    
    print("       MAIN MENU        ".center(73," "))
    print(" -----------------------".center(73," "))
    print(" 1. ADD STUDENT         ".center(73," "))
    print(" 2. FIND STUDENT        ".center(73," "))
    print(" 3. DELETE STUDENT      ".center(73," "))
    print(" 4. UPDATE STUDENT      ".center(73," "))
    print(" 5. DISPLAY ALL STUDENT ".center(73," "))
    print(" 0. QUIT/END            ".center(73," "))
    print(" -----------------------".center(73," "))
    #for i in range(1,5):print(" "*73)
    
def addstudent()->None:
    system('cls')
    for i in range(1,5):print(" "*73)
    print("Add Student           ".center(73))
    print("----------------------".center(73))
    print(" "*25,end="")
    idno:str = input("IDNO      :")
    print(" "*25,end="")
    lastname:str = input("LASTNAME  :")
    print(" "*25,end="")
    firstname:str = input("FIRSTNAME :")
    print(" "*25,end="")
    course:str = input("COURSE    :")
    print(" "*25,end="")
    level:str = input("LEVEL     :")
    ok:bool = slist.addstudent(Student(idno,lastname,firstname,course,level))
def displayall()->None:
    system('cls')
    slist.showlist()
def main()->None:
    
    option:str = ""
    while option !="0":
        displaymenu()
        print(" "*25,end="")
        option=input(" Enter Option(0..5):   ")
        match option:
            case "1": addstudent()
            case "2": pass
            case "3": pass
            case "4": pass
            case "5": displayall()
            case "0": print("Program Ended".center(73))
            case   _: print("Invalid Option".center(73))
        print(" "*25,end="")
        print(end="")
        input("press any key to continue...")
            
if __name__=="__main__":
    main()