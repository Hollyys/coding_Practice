# ver1
def solution(want, number, discount):
    answer = 0
    dlen = len(discount)
    
    for i in range(dlen-10+1):
        count = [0] * len(want)
        for index in range(i, i+10):
            if discount[index] in want:
                count[want.index(discount[index])] += 1
                
            if count == number:
                answer += 1
                break
            
    return answer

# ver2
def solution(want, number, discount):
    answer = 0
    n = len(discount)
    
    for i in range(n-10+1):
        dict = {}
        for j in range(i, i+10):
            thing = discount[j]
            if thing in dict:
                dict[thing] += 1
            else:
                dict[thing] = 1
        flag = True
        for j in range(len(want)):
            if not want[j] in dict or number[j] > dict[want[j]]:
                flag = False
        if flag:
            answer += 1
            
    return answer