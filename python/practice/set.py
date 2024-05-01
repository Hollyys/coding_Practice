visited1 = set()
visited2 = set()

print(visited1)
print(visited2)

data = (1,2)
visited1.add(data)
print('visited1:', visited1)
visited2 = visited2|{data}
print('visited2:', visited2)

visited1.add(data)
print('visited1:', visited1)
visited2 = visited2|{data}
print('visited2:', visited2)

data = (3,4)
visited1.add(data)
print('visited1:', visited1)
visited2 = visited2|{data}
print('visited2:', visited2)

data = (5,6)
visited1.add(data)
print('visited1:', visited1)
visited2 = visited2|{data}
print('visited2:', visited2)

set1  = set([1,2,3,4,5,6])
set2  = set([3,4,5,6,8,9])

print('교집합:\t\t', set1 & set2)
print('합집합:\t\t', set1 | set2)
print('차집합:\t\t', set1 - set2)
print('대칭차집합:\t', set1 ^ set2)