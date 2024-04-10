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

# ver 2:
# 딕셔너리의 remove 기능을 통해
# 반복문을 조절하여 효율성 향상

from collections import deque
                
def solution(n, wires):
    answer = float('inf')
    def dfs(tree):
        visited = [False] * (n+1)
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
    tree = {}
    for i in range(1,n+1):
        tree[i] = []
    for wire in wires:
        a, b = wire[0], wire[1]
        tree[a].append(b)
        tree[b].append(a)
    for wire in wires:
        a, b = wire[0], wire[1]
        tree[a].remove(b)
        tree[b].remove(a)
        m = dfs(tree)
        answer = min(answer, abs(m-(n-m)))
        tree[a].append(b)
        tree[b].append(a)
        
    return answer