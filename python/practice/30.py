# Ver 1
from collections import deque

def path(sx, sy, dx, dy, map):
    # 시작지점에서 목적지점까지 최단 경로 탐색
    # 경로 없으면 -1 출력
    ddx, ddy = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append((sx, sy, 0))
    # print(sx, sy, "출발 0")
    
    m = len(map)
    n = len(map[0])
    visited = [[False]*n for _ in range(m)]
    visited[sx][sy] = True
    
    while q:
        x, y, cost = q.popleft()
        
        if x == dx and y == dy:
            # print(x, y, "도착", cost)
            # print()
            return cost
        
        for i in range(4):
            nx = x + ddx[i]
            ny = y + ddy[i]
            
            if 0 <= nx < m and 0 <= ny < n and map[nx][ny] !='X':
                if not visited[nx][ny]:	# 아직 방문하지 않는 통로라면
                    q.append((nx, ny, cost+1))
                    # print(nx, ny, "방문", cost+1, q)
                    visited[nx][ny] = True
                    
    return -1	# 탈출할 수 없다면

def solution(maps):
    answer = 0
    
    for x in range(len(maps)):
        for y in range(len(maps[x])):
            if maps[x][y] == "S":
                sx, sy = x, y
            elif maps[x][y] == "L":
                lx, ly = x, y
            elif maps[x][y] == "E":
                ex, ey = x, y
    
    path1 = path(sx, sy, lx, ly, maps)
    path2 = path(lx, ly, ex, ey, maps)
    if path1 == -1 or path2 == -1:
        answer = -1
    else:
        answer = path1 + path2
    return answer

# Ver 2: 실패
from collections import deque

def route(start, exit, maps, visited):
    m = len(maps)
    n = len(maps[0])
    q = deque()
    cx, cy = start
    q.append((cx, cy, 0))
    while q:
        cx, cy, cn = q.popleft()
        visited[cx][cy] = False
        if (cx,cy) == exit:
            return cn
        if 0 <= cx-1 and visited[cx-1][cy] and maps[cx-1][cy] != 'X':
            q.append((cx-1,cy,cn+1))
        if 0 <= cy-1 and visited[cx][cy-1] and maps[cx][cy-1] != 'X':
            q.append((cx,cy-1,cn+1))
        if cx+1 < m and visited[cx+1][cy] and maps[cx+1][cy] != 'X':
            q.append((cx+1,cy,cn+1))
        if cy+1 < n and visited[cx][cy+1] and maps[cx][cy+1] != 'X':
            q.append((cx,cy+1,cn+1))
    return -1

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    visited = [[True for _ in range(n)] for _ in range(m)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
            if maps[i][j] == 'E':
                exit = (i,j)
    
    mid = route(start, lever, maps, visited)
    print(mid)
    if mid == -1:
        return -1
    end = route(lever, exit, maps, visited)
    print(end)
    if end == -1:
        return -1
                
    return mid + end

# Ver 3
from collections import deque

def route(start, exit, maps):
    cx, cy = start
    
    m = len(maps)
    n = len(maps[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[cx][cy] = True
    
    q = deque()
    q.append((cx, cy, 0))
    
    while q:
        cx, cy, cn = q.popleft()
        if (cx,cy) == exit:
            return cn
        
        if 0 <= cx-1 and not visited[cx-1][cy] and maps[cx-1][cy] != 'X':
            q.append((cx-1,cy,cn+1))
            visited[cx-1][cy] = True
        if 0 <= cy-1 and not visited[cx][cy-1] and maps[cx][cy-1] != 'X':
            q.append((cx,cy-1,cn+1))
            visited[cx][cy-1] = True
        if cx+1 < m and not visited[cx+1][cy] and maps[cx+1][cy] != 'X':
            q.append((cx+1,cy,cn+1))
            visited[cx+1][cy] = True
        if cy+1 < n and not visited[cx][cy+1] and maps[cx][cy+1] != 'X':
            q.append((cx,cy+1,cn+1))
            visited[cx][cy+1] = True
            
    return -1

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
            if maps[i][j] == 'E':
                exit = (i,j)
    
    mid = route(start, lever, maps)
    if mid == -1:
        return -1
    end = route(lever, exit, maps)
    if end == -1:
        return -1
                
    return mid + end