class Student():
    def __init__(self):
        self.id = 1
        self.name= 'Abdul Rehman'
        print("Parent Class Constructor Called")
    def printstatement(self):
        print('ID: ',self.id,'Name: ',self.name)        
#----------------
# BS extends Student so Student is Parent and BS is child
#---------------

class BS(Student):
    def __init__(self):
        # self.id
        # self.name
        super().__init__()
        self.degree = 'BS'        
    def printBs(self):
        self.printstatement()
        print('Degree: ',self.degree)
#start of main
# if __name__ == '__main__':
# student = Student()
b1 = BS()
# print(b1.degree)
b1.printBs()
# student.printstatement()