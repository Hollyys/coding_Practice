from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    n = len(progresses)
    
    for i in range(n):
        if (100-progresses[i])%speeds[i] != 0:
            left = (100-progresses[i])//speeds[i]+1
        else:
            left = (100-progresses[i])//speeds[i]
        q.append(left)
    
    max = q.popleft()
    cnt = 1
    while q:
        pop = q.popleft()
        if pop <= max:
            cnt += 1
        else:
            max = pop
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
            
    return answer