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