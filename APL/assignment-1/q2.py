'''
 @author 20021519-101
 Write a program to create a menu-driven calculator for +,-,*,/.
'''
def num1():
    return input('Enter the Number-1: ')
def num2():
    return input('Enter the Number-2: ')
def add():
    return int(num1())+int(num2())
def subs():
    return int(num1())-int(num2())
def Mul():
    return int(num1())*int(num2())
def div():
    return int(num1())/int(num2())
def menu():
    print('''
          1) Addition
          2) Substraction
          3) Multiplication
          4) Division
          ''')
def main():
    again = 'Y'
    while again == 'Y':
        menu()
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            print("Answer",add())
        elif choice == 2:
            print("Answer",subs())
        elif choice == 3:
            print("Answer",Mul())
        elif choice == 4:
            print("Answer",div())
        else:
            print('Wrong input!!! Try again')
            menu()
        again = input('Do you want to run Again?[Y/N}')
main()
