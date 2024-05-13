import functools

def compare(a, b):
    la, lb = len(a), len(b)
    return (la>lb) - (la<lb)

def solution(s):
    answer = []
    tmp = []
    
    input = []
    string = ''
    
    for x in s:
        if '0'<=x<='9':
            string += x
        elif x==',' and len(string) > 0:
            input.append(int(string))
            string = ''
        elif x=='}' and len(string) > 0:
            input.append(int(string))
            string = ''
            tmp.append(input)
            input = []
    tmp = sorted(tmp, key=functools.cmp_to_key(compare))
    
    for x in tmp:
        for y in x:
            if y not in answer:
                    answer.append(y)
    return answer

# Ver2: 불 필요한 코드 정리
def solution(s):
    answer = []
    tmp = []
    
    input = []
    string = ''
    
    for x in s:
        if '0'<=x<='9':
            string += x
        elif x==',' and len(string) > 0:
            input.append(int(string))
            string = ''
        elif x=='}' and len(string) > 0:
            input.append(int(string))
            string = ''
            tmp.append(input)
            input = []
    tmp = sorted(tmp, key=len)
    
    for x in tmp:
        for y in x:
            if y not in answer:
                    answer.append(y)
    return answer

# Ver3: split 알고리즘 활용
def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)
    
    for x in s:
        data = x.split(',')
        for y in data:
            if int(y) not in answer:
                answer.append(int(y))
                    
    return answer