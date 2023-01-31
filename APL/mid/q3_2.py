my_list = [22.4,4.0,16.22,9.1,11.0,12.22,14.2,5.2,17.5]

print("Original List: ",my_list)
rounded_list = [round(num) for num in my_list]
print("Rouned List: ",rounded_list)
print("Max Number: ",max(rounded_list))
print("Min Number: ",min(rounded_list))