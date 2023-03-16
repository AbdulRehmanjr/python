from functools import reduce 

class Person:
    
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address

    def getName(self)->str:
        return self.name
    
    def getAddress(self)->str:
        return self.address
    
    def setAddress(self,address):
        self.address = address
        
    def __str__(self) -> str:
        return  f"Name : {self.name}, Address: {self.address}"

class Student(Person):
    
    def __init__(self, name, address) -> None:
        super().__init__(name, address)
        
        self.numCourses = 0 
        self.courses = []
        self.grades = []

    def __str__(self) -> str:
        return f"Student: {super().__str__()}"
    
    def addCourseGrade(self,course,grade):
        if course not in self.courses:
            self.numCourses=self.numCourses+1
            self.courses.append(course)
            self.grades.append(grade)
    
    def printGrades(self):
        
        print("[*] Printing the Course with respective Grades")
        for course,grade in zip(self.courses,self.grades):
            print(f"[*] {course} : {grade}")
            
        
    
    def getAverageGrades(self)->float:
        cal_sum = lambda x,y : x+y
        total = reduce(cal_sum,self.grades)
        average = total/len(self.grades)
        return average
        
class Teacher(Person):
    
    def __init__(self, name, address) -> None:
        super().__init__(name, address)

        self.numCourses = 0
        self.courses = []
        
    def __str__(self) -> str:
        return f"Teacher: {super().__str__()}"
    
    def addCourse(self,course)->bool:
        
        if course not in self.courses:
            print("[*] Adding course")
            self.courses.append(course)
            self.numCourses = self.numCourses + 1
            return True
        
        return False
    
    def removeCourse(self,course)->bool:
        
        if course in self.courses:
            print("[*] Removing course")
            self.courses.remove(course)
            self.numCourses = self.numCourses - 1
            return True
        
        return False    
    
    
if __name__ =='__main__':
    
    teacher = Teacher("Mr. Najeeb ur Rehman","UOG")
    
    student = Student("Abdul Rehman","Ghakhar")
    
    teacher.addCourse("APL")
    teacher.addCourse("IS")
    
    print("[*] Teacher Info")
    print(teacher.__str__())
    
    student.addCourseGrade("APL",85)
    student.addCourseGrade("IS",85)
    
    
    
    print("[*] Student Info")
    print(student.__str__())
    
    print(f"[*] Average grade : {student.getAverageGrades()}")
    