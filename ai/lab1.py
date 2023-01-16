#  lab 1 task 
class Student():
    def __init__(self,name,roll,age,section):
        self.studentName = name
        self.studentRoll = roll
        self.studentAge = age
        self.studentSection = section                    
    def __str__(self):
        return "{0},{1},{2},{3}".format(self.studentName, self.studentRoll,self.studentAge, self.studentSection)    
# funcations of main   
def display():
    print('''
          1 = Display data
          2 = Enter new Record
          3 = Delete the Data
          4 = Update Data
          5 = Exit program
          ''')
def choices(choice):
    if choice == 1:
        display_result(studentList) 
    elif choice == 2:
        append_record(studentList)
    elif choice == 3:
        display_result(studentList)
        try:
            position = int(input('Enter the position:'))
            delete_record(studentList,position)
        except ValueError:
            print('Error invalid input')    
    elif choice == 4:
        try:
            position = int(input('Enter the position:'))
            update_record(studentList,position)
        except ValueError:
            print('Error invalid input')
    elif choice == 5:
        exit()   
    else:
        print('Invalid choice:')
     
#display records                             
def display_result(list):
    index = 1
    print ("{:<5} {:<15} {:<15} {:<10} {:<10}".format('Index','Name','Roll','Age','Section'))
    print ("------------------------------------------------")
    for student in list:
        print("{:<5} {:<15} {:<15} {:<10} {:<10}".format(index,student.studentName, student.studentRoll, student.studentAge, student.studentSection))
        index = index+1

def take_input():
    try:
        name = input('Enter the Student Name')
        age =  int(input('Enter the Student Age'))
        roll = input('Enter the roll aaaaaaaa-aaa')
        section = input('Enter the Section -:')  
        return Student(name,roll,age,section)
    except ValueError:
        print('Error Invalid Input')    
# add record        
def append_record(list):
    list.append(take_input())
# delete records        
def delete_record(list,position):
    index = 1
    if position > len(list):
        print('Number is greater than the records in list')
    else:
        for student in list:
            print('okay?')
            if index == position:
                list.remove(student)
                break
            index = index+1       
def update_record(list,position):
    if position > len(list):
        print('Number is greater than the records in list')
    else:
        list[position-1] = take_input()
if __name__ == '__main__':
    studentList = []
    studentList.append(Student('Abdul Rehman','20021519-101',20,'C'))
    studentList.append(Student('Muhammad Umar','20021519-139',20,'C'))
    studentList.append(Student('Khizar','20021519-003',20,'C'))
    studentList.append(Student('Usama','20021519-031',20,'C'))
    studentList.append(Student('Muneer','20021519-008',20,'C'))
    showDisplay = True
    while showDisplay:
        display()
        try:
            choice = int(input("Enter Your choice"))
            choices(choice)
            again = input('Do You want to Run again[y/n]?')
            if again != 'y':
                showDisplay = False
        except ValueError:
            print('Error Please Pass a Number given in Menu')
        