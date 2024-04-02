#  실패
from collections import deque

def bfs(answer, visited, tree, n, costs):
    q = deque()
    q.append((0, 0, visited))
    
    while q:
        loc, dist, visit = q.popleft()
        visit.add(loc)
        if len(visit) == n and dist < answer:
            print(loc, ':', dist, visit, ': 조건 만족')
            answer = dist
        else:
            print(loc, ':', dist, visit)
        
        for d in tree[loc]:
            if d[0] not in visit:
                print(d, visit)
                q.append((d[0], dist+d[1], visit))
        print(q)
        print()
    return answer

def solution(n, costs):
    answer = (((n-1) * n) / 2) * 10**10
    visited = set()
    tree = {}
    for i in range(n):
        tree[i] = []
    
    for cost in costs:
        tree[cost[0]].append((cost[1], cost[2]))
        tree[cost[1]].append((cost[0], cost[2]))
        
    print(tree)
    print()
                 
    return bfs(answer, visited, tree, n, costs)

# 컨닝

def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[xroot] = yroot
        rank[yroot] += 1
        
    return None
    
def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    
    parent = [i for i in range(n)]
    rank = [0] * n
    
    min_cost = 0
    edges = 0
    
    for edge in costs:
        if edges == n-1:
            break
            
        rootx = find(parent, edge[0])
        rooty = find(parent, edge[1])
        
        if rootx != rooty:
            union(parent, rank, rootx, rooty)
            min_cost += edge[2]
            edges += 1
                 
    return min_cost