

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
        return  f"Name : ${self.name}, Address: ${self.address}"

class Student(Person):
    
    def __init__(self, name, address) -> None:
        super().__init__(name, address)
        
        self.numCourses = 0 
        self.courses = []
        self.grades = []

    def __str__(self) -> str:
        return f"Student: ${super().__str__()}"
    
    def addCourseGrade(self,course,grade):
        if course not in self.courses:
            self.numCourses=self.numCourses+1
            self.courses.append(course)
            self.grades.append(grade)
    
    def printGrades(self):
        
        print("[*] Printing the Course with respective Grades")
        for course,grade in zip(self.courses,self.grades):
            print(f"[*] ${course} : ${grade}")
            
        
    
    def getAverageGrades(self)->float:
        g = 0
        cal_sum = lambda x:x+g
        total = cal_sum(self.grades)
        average = total/len(self.grades)
        return average
        
class Teacher(Person):
    
    def __init__(self, name, address) -> None:
        super().__init__(name, address)

        self.numCourses = 0
        self.courses = []
        
    def __str__(self) -> str:
        return f"Teacher: ${super().__str__()}"
    
    def addCourse(self,course)->bool:
        
        
        return True
    
    def removeCourse(self,course)->bool:
        
        return True
    






if __name__ =='__main__':
    pass