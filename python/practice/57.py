def solution(n):
    answer = ''
    number = []
    string = str(n)
    for x in string:
        number.append(x)
    
    number = sorted(number)
    number.reverse()
    
    for x in number:
        answer += x
        
    return int(answer)