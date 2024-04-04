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
        # visited[cn][cm] = True
        if cn == n-1 and cm == m-1:
            return dist
        
        for i in range(4):
            wn, wm = cn+way[i][0], cm+way[i][1]
            if 0<=wn<n and 0<=wm<m and not visited[wn][wm] and maps[wn][wm] == 1:
                visited[wn][wm] = True
                q.append([wn, wm, dist+1])
        
    return -1

# pop 하는 모든 좌표에 대해 방문 기록을 남기는 것 보다
# append 하는 좌표에 대해서만 기록을 남기는 것이 낫다.
# 왜냐하면 append 좌표는 특정 조건에 대해 한번 걸러진
# 원소들이기 때문에 경로의 경우의 수가 매우 많아질 경우,
# 연산량이 기하급수적으로 늘어나게 된다.