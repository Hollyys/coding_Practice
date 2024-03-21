# 실패
from collections import deque

def solution(info, edges):
    answer = 0
    
    n_sheep = 0
    n_wolf = 0
    visited = [[False] for _ in range(len(info))]
    
    for i in info:
        if i == 0:
            n_sheep += 1
        else:
            n_wolf += 1
    
    tree = {[] for _ in range(len(info))}
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    q = deque()
    q.append((0, 1, 0))
    visited[0] = True
    
    while q:
        idx, sheep, wolf = q.popleft()
        answer = max(answer, sheep)
        for i in range(len(tree[idx])):
            if not visited[tree[idx][i]]:
                if info[tree[idx][i]] == 0:
                    q.append((tree[idx][i],sheep+1,wolf))
                    visited[tree[idx][i]] = True
                elif sheep > wolf + 1:
                    q.append((tree[idx][i],sheep,wolf+1))
                    visited[tree[idx][i]] = True
            else:
                q.append((tree[idx][i],sheep,wolf))
        
    return answer