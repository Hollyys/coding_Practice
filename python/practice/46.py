from collections import deque
def dfs(tree, visited):
    cnt = 1
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        node = q.pop()
        for child in tree[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True
                cnt += 1
    return cnt
                
def solution(n, wires):
    answer = float('inf')
    for idx in range(len(wires)):
        tree = {}
        visited = [False] * (n+1)
        for i in range(1,n+1):
            tree[i] = []
        for index, wire in enumerate(wires):
            if idx != index:
                a, b = wire[0], wire[1]
                tree[a].append(b)
                tree[b].append(a)      
        m = dfs(tree, visited)
        answer = min(answer, abs(m-(n-m)))
    return answer