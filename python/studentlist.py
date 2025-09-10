'''
	StudentList
'''
from student import Student

class StudentList:
    def __init__(self,size)->None: 
        self.slist = [] #data container
        self.size = size
        
    #sentinel modules
    def isempty(self)->bool:    return len(self.slist)==0
    def isfull(self)->bool:     return len(self.slist)==self.size
    #utility modules
    def addstudent(self,s:Student)->bool:
        ok:bool=not self.isfull()
        if ok:
            self.slist.append(s)
        return ok
            
    def findstudent(self,idno:str)->Student:
        ok:bool = not self.isempty()
        if ok:
            for student in slist:
                if student.getidno() == idno:
                    return student
                    break
        return None
        
    def deletestudent(self,idno:str)->bool:
        ok:bool = False
        student:Student = self.findstudent(idno)
        if student != None:
            self.slist.remove(student)
            ok=True
        return ok
            
    def updatestudent(self,s:Student)->bool:
        ok:bool = False
        student:Student = self.findstudent(s.getidno())
        if student != None:
            index:int = self.slist(student)
            self.slist[index]=s
            ok=True
        return ok
        
    #
    def showlist(self)->list:
        if not self.isempty():
            for student in self.slist:
                print(f"{student.getidno()} {student.getlastname()} {student.getfirstname()} {student.getcourse()} {student.getlevel()}")



