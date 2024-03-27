from collections import defaultdict, deque

def bfs(tree, start, result):
    q = deque()
    q.append(start)
    result.append(start)
    while q:
        node = q.popleft()
        if node in tree:
            for child in tree[node]:
                if child not in result:
                    result.append(child)
                    q.append(child)
    return None

def solution(graph, start):
    result = []
    tree = {}

    for node in graph:
        parent = node[0]
        child = node[1]
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
    print(tree)
    bfs(tree, start, result)
    return result

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],1))
print('반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]')

print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],1))
print('반환값 : [1, 2, 3, 4, 5, 0]')