# Ver 1: 알고리즘은 맞았으나 시간초과
from collections import deque

def solution(N, road, K):
    answer = 0
    # road.sort(key = lambda x: x[0])
    
    def bfs(start, end, visited):
        q = deque()
        q.append([1, 0])
        while q:
            pop = q.popleft()
            cloc, dist = pop[0], pop[1]
            if cloc == end:
                return dist
            for data in road:
                if data[0] == cloc and not visited[data[1]] and (dist+data[2]) <= K:
                    visited[data[1]] == True
                    q.append([data[1], dist+data[2]])
                elif data[1] == cloc and not visited[data[0]] and (dist+data[2]) <= K:
                    visited[data[0]] == True
                    q.append([data[0], dist+data[2]])

        return -1
    
    for side in range(1, N+1):
        visited = [False]*(N+1)
        visited[1] = True
        dist = bfs(1, side, visited)
        if dist != -1:
            answer += 1

    return answer

# Ver 2:
# 이거는 알고리즘이 틀렸다.
# 한번 방문한 노드를 다시 거쳐서 가야 도달할 수 있는 경우가 있을 수 있다.
from collections import deque

def solution(N, road, K):
    answer = 0
    visited = [False] * (N+1)
    
    q = deque()
    q.append([1,0])
    visited[1] = True
    answer += 1
    
    while q:
        pop = q.popleft()
        cloc, dist = pop[0], pop[1]
        for data in road:
            if data[0] == cloc and not visited[data[1]] and (dist+data[2]) <= K:
                visited[data[1]] = True
                q.append([data[1], dist+data[2]])
                answer += 1
            elif data[1] == cloc and not visited[data[0]] and (dist+data[2]) <= K:
                visited[data[0]] = True
                q.append([data[0], dist+data[2]])
                answer += 1

    return answer