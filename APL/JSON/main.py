import json
import pandas as pd
import sys

# model class


class Student:

    def __init__(self, studentName, fatherName, studentDob, studentAddress, studentPhone, studentGender, studentSection, studentBatch, studentRoll):
        self.studentId = 0
        self.studentName = studentName
        self.fatherName = fatherName
        self.studentDob = studentDob
        self.studentAddress = studentAddress
        self.studentPhone = studentPhone
        self.studentGender = studentGender
        self.studentSection = studentSection
        self.studentBatch = studentBatch
        self.studentRoll = studentRoll

    def __str__(self) -> dict:
        student = {
            "studentId": self.studentId,
            "studentName": self.studentName,
            "fatherName": self.fatherName,
            "studentDob": self.studentDob,
            "studentAddress": self.studentAddress,
            "studentPhone": self.studentPhone,
            "studentGender": self.studentGender,
            "studentSection": self.studentSection,
            "studentBatch": self.studentBatch,
            "studentRoll": self.studentRoll
        }
        return student


# view class
class StudentView:

    def __init__(self) -> None:
        self.studentController = StudentController()

    '''Display Block '''

    # logo
    def logoDisplay(self):
        '''display logo of project'''

        print('''
              Welcome to Student Record Management 
                        JSON
                    By 20021519-101
              ''')

    # main menu display
    def mainDisplay(self):
        '''display the menu of project'''

        print('''
              1) View Records
              2) Add new Record
              3) Update Record
              4) Delete Record
              5) Exit
              ''')

    def recordView(self):
        '''Record View menu'''

        print('''
              1) Find all
              2) Find By Id
              3) Find By Name
              4) Find By Father Name
              5) Find By Roll
              6) Find By Section
              7) Go Back
              ''')

    def updateView(self):
        '''Update View menu'''

        print('''
              1) Update all information 
              2) Update  Id
              3) Update Name
              4) Update Father Name
              5) Update Roll
              6) Update Section
              7) Go Back
              ''')
    '''Choice Block'''

    def updateChoice(self):
        '''Get the functions linked with given choice'''

        choice = int(input('Enter your choice: '))
        id = self.studentController.numberInput('Student Id to find record')
        self.studentController.findRecord('studentId', id)
        if choice == 1:
            self.studentController.updateAll(
                self.studentController.inputStudent(), id)
        elif choice == 2:
            self.studentController.updateRecord(
                'studentId', id, self.studentController.stringInput('Student Id'))
        elif choice == 3:
            self.studentController.updateRecord(
                'studentName', id, self.studentController.stringInput('Student Name'))
        elif choice == 4:
            self.studentController.updateRecord(
                'fatherName', id, self.studentController.stringInput('Father Name'))
        elif choice == 5:
            self.studentController.updateRecord(
                'studentRoll', id, self.studentController.stringInput('Student Roll'))
        elif choice == 6:
            self.studentController.updateRecord(
                'studentSection', id, self.studentController.stringInput('Student Section'))
        elif choice == 7:
            self.choiceSelection()
        else:
            self.inValidChoiceError()
            self.recordChoice()

    def recordChoice(self):
        '''Get the functin linked with given choice'''

        choice = int(input('Enter your choice: '))
        if choice == 1:
            self.studentController.showRecord()
        elif choice == 2:
            id = self.studentController.numberInput('Student Id')
            self.studentController.findRecord('studentId', id)
        elif choice == 3:
            name = self.studentController.stringInput('Student Name')
            self.studentController.findRecord('studentName', name)
        elif choice == 4:
            fname = self.studentController.stringInput('Father Name')
            self.studentController.findRecord('studentName', fname)
        elif choice == 5:
            roll = self.studentController.stringInput('Roll Number')
            self.studentController.findRecord('studentRoll', int(roll))
        elif choice == 6:
            section = self.studentController.stringInput('Student Section')
            self.studentController.findRecord('studentSection', section)
        elif choice == 7:
            self.choiceSelection()
        else:
            self.inValidChoiceError()
            self.recordChoice()

    def choiceSelection(self):
        '''show menu and get choice'''
        self.mainDisplay()
        try:
            choice = int(input('Enter your choice: '))
            self.choiceFunction(choice)
        except ValueError:
            self.inValidChoiceError()
            self.choiceSelection()

    def choiceFunction(self, choice):
        '''get the functin linked with given choice'''
        if choice == 1:
            self.recordView()
            self.recordChoice()
        elif choice == 2:
            self.studentController.saveStudent(
                self.studentController.inputStudent())
        elif choice == 3:
            self.updateView()
            self.updateChoice()
        elif choice == 4:
            id = self.studentController.numberInput(
                'Student Id to delete record')
            self.studentController.deleteRecord('studentId', id)
        elif choice == 5:
            sys.exit()
        else:
            self.inValidChoiceError()
            self.choiceSelection()

    '''Exception Block'''

    # invalid choice exception
    def inValidChoiceError(self):
        '''Exception message nvalid choice'''
        print('''Invalid choice !!!!!
                Try Again 
            ''')

# controller class


class StudentController:

    def __init__(self) -> None:
        self.path = './student.json'
        self.idFile = './id.txt'

    '''Input Section'''
    # string input

    def stringInput(self, message) -> str:
        sin = input(f'Enter the {message}: ')
        return sin

    # string input
    def numberInput(self, message) -> int:
        try:
            iin = int(input(f'Enter the {message}: '))
        except ValueError:
            print('Value Error Try again')
            iin = self.numberInput(message)
        return iin
    # input student and return

    def inputStudent(self) -> Student:
        '''Input data and return Student'''

        name = self.stringInput('Student Name')
        fname = self.stringInput('Father Name')
        dob = self.stringInput('DOB [DD/MM/YYYY]')
        address = self.stringInput('Address')
        phone = self.stringInput('Phone No.')
        gender = self.stringInput('Gender')
        section = self.stringInput('Section')
        batch = self.stringInput('Batch')
        roll = self.stringInput('Roll No.')

        student = Student(name, fname, dob, address, phone,
                          gender, section, batch, roll)

        return student
    '''
    CREATE SECTION START
    '''
    # create a new record single

    def saveStudent(self, data: Student):
        '''save a new Student Record'''
        data.studentId = self.generateId()
        self.appendJsonFile(data)

    # append to json fie
    def appendJsonFile(self, data: Student):
        '''append json data to existing file'''
        # get data from file
        with open(self.path, "r") as file:
            oldData = json.load(file)
        oldData.append(data.__str__())
        # write the data
        with open(self.path, "w") as file:
            json.dump(oldData, file, indent=2)

    # auto generat id
    def generateId(self) -> int:
        '''return a unique id increment from existing one'''
        id = 0
        try:
            with open(self.idFile, "r") as file:
                id = int(file.read())
        except FileNotFoundError:
            print('File not found error')
        try:
            with open(self.idFile, "w") as file:
                newId = id+1
                file.write(str(newId))
        except FileNotFoundError:
            print('File not found error')

        return id
    '''
    CREATE SECTION END
    '''
    '''
    READ SECTION START
    '''
    # read data from file

    def showRecord(self):
        data = pd.read_json('./student.json')
        print(data)

    # find record a generic code ==> id,dob etc all in one
    def findRecord(self, findBy, value):
        data = pd.read_json('./student.json')
        try:
            data = data.loc[data[findBy] == value]
            print(data)
        except ValueError:
            print(f'No student registered with {findBy}: {value}')
    '''
    READ SECTION END
    '''

    '''
    UPDATE SECTION START
    '''

    def updateRecord(self, updateBy, id, newValue):
        with open('./student.json', "r") as fileData:
            oldData = json.load(fileData)
            for data in oldData:
                if (data["studentId"] == id):
                    data[updateBy] = newValue
                    break
        with open(self.path, "w") as file:
            json.dump(oldData, file, indent=2)

    def updateAll(self, student, id):
        with open('./student.json', "r") as fileData:
            oldData = json.load(fileData)
            for data in oldData:
                if (data["studentId"] == id):
                    data = student
                    break
        with open(self.path, "w") as file:
            json.dump(oldData, file, indent=2)
    '''
    UPDATE SECTION END
    '''
    '''
    DELETE SECTION START
    '''

    def deleteRecord(self, deleteBy, value):
        with open('./student.json', "r") as fileData:
            oldData = json.load(fileData)
            for data in oldData:
                if (data[deleteBy] == value):
                    oldData.remove(data)
                    break
        with open(self.path, "w") as file:
            json.dump(oldData, file, indent=2)
    '''
    DELETE SECTION START
    '''
# auto generated file ==> id


def createIdFile():
    path = './id.txt'
    try:
        with open(path, "r") as file:
            pass
    except FileNotFoundError:
        with open(path, "w") as file:
            file.write("1")

# create JsonFile


def createJsonFile():
    filePath = "./student.json"
    '''Create a empty json file if not exists and write a []'''
    data = []
    try:
        with open(filePath, "r") as file:
            pass
    except FileNotFoundError:
        with open(filePath, "w") as file:
            json.dump(data, file)


if __name__ == "__main__":
    createIdFile()  # id file creation one time
    createJsonFile()  # json creation one time
    display = StudentView()
    display.logoDisplay()
    choice = 'y'
    while choice == 'y':
        display.choiceSelection()
        choice = input('Press y to continue:')
