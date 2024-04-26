from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations

l = [1,2,3,4]

print('\ncombinations')
n = 0
for i in combinations(l,2):
    n += 1
    print(i)
print('n:', n)

print('\ncombinations_with_replacement')
n = 0
for i in combinations_with_replacement(l,2):
    n += 1
    print(i)
print('n:', n)
    
print('\npermutations')
n = 0
for i in permutations(l,2):
    n += 1
    print(i)
print('n:', n)
    
print('\npermutations')
print('r을 지정하지 않거나 r=None으로 하면 최대 길이의 순열이 리턴된다')
n = 0
for i in permutations(l):
    n += 1
    print(i)
print('n:', n)