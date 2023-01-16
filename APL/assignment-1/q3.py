'''
@author 20021519-101
 File Handling (Reading/Writing) [https://docs.python.org/3/tutorial/inputoutput.html]

   i. Create an input file with a minimum of 3 columns (int, float, string) and 15 records. Order of columns can be of your own choice.

  ii. Read this file appropriately using basic concepts of python.

 iii. Three columns should be considered 3 different lists of appropriate data types.

  iv. Perform basic operations (https://realpython.com/python-lists-tuples/)  on lists as discussed in class.

   v. Write these modified lists into a file.

  vi. You can write the file as JSON Objects and read it for your learning. (Optional)
'''

def readFile():
    file = open('./info.txt')
    serials = []
    names = []
    cgpas = []
    # reading the lines as list
    lines = file.readlines()
    file.close()
    #looping through list of lines
    for line in lines:
        # split returns a list of splited atributes can be access through list[index]
        # split each line by space and assign by concept of unpacking
        sr,name,cgpa = line.split(' ')
        #add in list of serials as int
        serials.append(int(sr))
        # add in list as float 
        cgpas.append(float(cgpa))
        # add in list of names as string but not \n  ['sad','\n'][0] => sad
        # strip works same 
        names.append(name.strip())
        # print(sr)
        # print(name)
    print(serials)
    print(names)
    print(cgpas)
def writeFile():
    file = open('./info.txt','a')
    #file.write("5 Umar\n")
    sr = input("Enter the Serial Number: ")
    name = input("Enter the Name: ")
    cgpa = input("Enter the Cgpa: ")
    file.write(str(sr+" "+name+" "+cgpa+"\n"))
    file.close()    
def menu():
    print('''
          1) Read from File
          2) Write in File
          ''')
def main():
    again = 'Y'
    while again == 'Y':
        menu()
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            readFile()
        elif choice == 2:
            readFile()
            writeFile()
        else:
            print('Wrong input!!! Try again')
            menu()
        again = input('Do you want to run Again?[Y/N}')
main()
