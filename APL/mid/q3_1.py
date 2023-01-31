from random import randint
from collections import Counter

my_list = []
my_dict = {}
for _ in range(0,10):
    my_list.append(randint(0,6))
    
my_tuple = tuple(my_list)
sort = tuple(sorted(my_tuple))
count = Counter(sort)

print(count)
    