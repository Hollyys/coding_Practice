def dfs(ck, dungeons, visited):
    cnt = 0
    answer = 0
    for i in range(len(dungeons)):
        if ck >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            ck -= dungeons[i][1]
            cnt += 1
            answer = max(answer, cnt + dfs(ck, dungeons, visited))
            visited[i] = False
            ck += dungeons[i][1]
            cnt -= 1
    return answer

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, visited)