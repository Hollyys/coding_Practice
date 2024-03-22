def dfs(node, adj_list, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list.get(node, []):
      if neighbor not in visited:
        dfs(neighbor, adj_list, visited, result)

def solution(graph, start):
  adj_list = {}

  # DFS를 순회한 결과를 반환
  visited = set()
  result = []
  dfs(start, adj_list, visited, result)
  return result

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')) # 반환값 : ['A', 'B', 'C', 'D', 'E']
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']