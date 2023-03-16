import pandas as pd


class Student:
    
    def __init__(self,roll,name,email,dob,phone) -> None:
        self.roll = roll
        self.name = name
        self.email = email
        self.dob = dob
        self.phone = phone 
    
    def __str__(self) -> str:        
        return f"Student : roll = {self.roll},name = {self.name}, email ={self.email}, dob = {self.dob}, phone = {self.phone}"
    

if __name__ =='__main__':

    student_list = []
    data = pd.read_csv('./data.csv')
    
    def studentList()->list:
        
        for index, row in data.iterrows():
            student = Student(row['Roll'],row['Name'],row['Email'],row['DOB'],row['Mobile'])                
            student_list.append(student.__str__())
        return student_list
    
    def findStudent(name):
        try:
            print(data.loc[data['Name'] == name])
        except ValueError:
            print(f'No student registered with Name: {name}')
        
    
    name = input("[*] Enter the Name of Student: ")
    findStudent(name)
    print("\n\n")
    studentList()
    print("[*] Printing data....")
    print(student_list)
    