import functools
 
def numeric_compare(x,y):
    return x-y
def numeric_compare_reverse(x,y):
    return y-x
# cmp_to_key 함수에 사용될 기준함수는 리턴값이 항상 1, -1, 0 이어야한다.
# 좌항이 크면 1, 작으면 -1, 좌우항이 같으면 0을 출력해야함

l = [5,2,3]
print(sorted(l, key=functools.cmp_to_key(numeric_compare)))
print(sorted(l, key=functools.cmp_to_key(numeric_compare_reverse)))
print(sorted(l))

print(True - True) # 0
print(True - False) # 1
print(False - True) # -1