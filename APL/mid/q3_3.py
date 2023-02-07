import itertools
 

s = 'xyz'
 
nums = list(s)
permutations = list(itertools.combinations_with_replacement(nums,3))
print(permutations)
