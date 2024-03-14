# Ver 1
def solution(cards1, cards2, goal):
    answer = ''
    cursor1 = 0
    cursor2 = 0
    
    for token in goal:
        print(token)
        if cards1[cursor1] == token:
            answer = 'Yes'
            if cursor1 < len(cards1) - 1:
                cursor1 += 1
        elif cards2[cursor2] == token:
            answer = 'Yes'
            if cursor2 < len(cards2) - 1:
                cursor2 += 1
        else:
            answer = 'No'
            break
        
    return answer

# Ver2
from collections import deque
def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for token in goal:
        if q1 and q1[0] == token:
            q1.popleft()
        elif q2 and q2[0] == token:
            q2.popleft()
        else:
            return "No"
        
    return "Yes"