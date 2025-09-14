from student import Student

class StudentList:
    def __init__(self, size) -> None:
        self.slist = []  # data container
        self.size = size

    # sentinel modules
    def isempty(self) -> bool:
        return len(self.slist) == 0

    def isfull(self) -> bool:
        return len(self.slist) == self.size

    # utility modules
    def addstudent(self, s: Student) -> bool:
        if not self.isfull():
            self.slist.append(s)
            return True
        return False

    def findstudent(self, idno: str) -> Student:
        for student in self.slist:
            if student.getidno() == idno:
                return student
        return None

    def deletestudent(self, idno: str) -> bool:
        student = self.findstudent(idno)
        if student:
            self.slist.remove(student)
            return True
        return False

    def updatestudent(self, s: Student) -> bool:
        student = self.findstudent(s.getidno())
        if student:
            index = self.slist.index(student)
            self.slist[index] = s
            return True
        return False

    def showlist(self) -> None:
        if self.isempty():
            print("No students found.")
        else:
            print("IDNO     LASTNAME   FIRSTNAME   COURSE   LEVEL")
            print("-------------------------------------------")
            for student in self.slist:
                print(f"{student.getidno()} {student.getlastname()} {student.getfirstname()} {student.getcourse()} {student.getlevel()}")
