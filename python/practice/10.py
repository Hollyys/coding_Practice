def check(s):
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            p = stack.pop()
            if p != "(":
                return False
        elif c == "}":
            if not stack:
                return False
            p = stack.pop()
            if p != "{":
                return False
        else:
            if not stack:
                return False
            p = stack.pop()
            if p != "[":
                return False
            
    if stack:
        return False
    else:
        return True
    
def solution(s):
    answer = 0
    rot = s
    while True:
        if check(rot):
            answer += 1
        rot = rot[-1] + rot[:-1]
        if rot == s:
            break

    return answer