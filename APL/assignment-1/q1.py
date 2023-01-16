'''
@author 20021519-101
 Write a program for the age calculator (Years, Months, Days) using system date-time.
'''

from datetime import date

birth_date = input("Enter your date of birth DD-MM-YYYY: ")
day,month,year = birth_date.split('-')
day = int(day)
month = int(month)
year = int(year)
current_date = date.today()
print(current_date.year)
age = current_date.year - year - ((current_date.month,current_date.day) < (month,day))
print('Your age is ',age)