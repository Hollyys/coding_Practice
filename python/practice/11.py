def solution(s):
    answer = 1
    stack = []

    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    
    if stack:
        answer = 0
    else:
        answer = 1

    return answer