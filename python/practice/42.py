from collections import deque

way = [[-1,0], [1,0], [0,-1], [0,1]]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    q = deque()
    q.append([0,0,1])
    visited[0][0] = True
    while q:
        pop = q.popleft()
        cn, cm, dist = pop[0], pop[1], pop[2]
        if cn == n-1 and cm == m-1:
            return dist
        
        for i in range(4):
            wn, wm = cn+way[i][0], cm+way[i][1]
            if 0<=wn<n and 0<=wm<m and not visited[wn][wm] and maps[wn][wm] == 1:
                visited[wn][wm] = True
                q.append([wn, wm, dist+1])
        
    return -1