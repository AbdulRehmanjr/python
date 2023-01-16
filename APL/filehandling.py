file = open('./files/info.txt')
serials = []
names = []
# reading the lines as list
lines = file.readlines()
file.close()
#looping through list of lines
for line in lines:
    # split returns a list of splited atributes can be access through list[index]
    # split each line by space and assign by concept of unpacking
    sr,name = line.split(' ')
    #add in list of serials as int
    serials.append(int(sr))
    # add in list of names as string but not \n  ['sad','\n'][0] => sad
    # strip works same 
    names.append(name.strip())
    # print(sr)
    # print(name)
print(serials)
print(names)
file = open('./files/info.txt','a')
#file.write("5 Umar\n")
sr = input("Enter the Serial Number: ")
name = input("Enter the Name: ")
file.write(str(sr+" "+name+"\n"))
file.close()