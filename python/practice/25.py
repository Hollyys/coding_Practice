from itertools import combinations

def combination(set, num):
    output = []
    temp = list(combinations(set, num))
    for element in temp:
        str = ""
        for i in element:
            str += i
        output.append(str)
    return output

def is_in(input, str):
    for alph in input:
        if alph not in str:
            return False
    return True

def solution(orders, course):
    answer = []
    x = set()
    menu = {}
    
    for order in orders:
        for a in order:
            x.add(a)
    alphabet = [x for x in sorted(x)]
    print(alphabet)
    
    for num in course:
        comb = combination(alphabet, num)
        for order in orders:
            for x in comb:
                if x not in menu:
                    menu[x] = 0
                if is_in(x, order):
                    menu[x] += 1
            
    for num in course:
        max = -1
        for element in menu:
            if len(element) == num and menu[element] > max:
                max = menu[element]
        if max < 2:
            break
        for element in menu:
            if len(element) == num and menu[element] == max:
                print(element, max)
                answer.append(element)
    return answer

import random

random_number = random.randint(0, 1)
if random_number == 1:  
    print("드라이브 ㄱㄱ")
else:
    print("오바임;;")

from itertools import combinations
from collections import Counter

sample_menu = "ABC"
for it in combinations(sample_menu):
    print(it)
    
counter = Counter(menu)  # ➌ 각 메뉴 구성이 몇 번 주문되었는지 세어줌