def solution(n, computers):
    answer = 0
    tree = {}
    for idx in range(n):
        tree[idx] = []
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] != 0:
                tree[i].append(j)
    print(tree)
    
    def dfs(start, group):
        visited[start] = True
        group.append(start)
        for child in tree[start]:
            if not visited[child]:
                dfs(child,group)
        return None
    
    for node in tree:
        if not visited[node]:
            group = []
            dfs(node, group)
            answer += 1

    return answer