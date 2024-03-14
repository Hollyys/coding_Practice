from collections import deque

def solution(N, K):
    q = deque(range(1,N+1))
    while len(q) > 1:
        for i in range(K-1):
            q.append(q.popleft())
        q.popleft()

    return q.popleft()
    
print(solution(5,2))