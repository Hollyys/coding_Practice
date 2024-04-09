# 실패: 어느 지점까지는 cost가 같다가
# 그 다음 부터 방향전환 계산 실패로 인한 오류
import heapq

def printdis(array_2d):
    column_widths = [max(map(len, map(str, column))) for column in zip(*array_2d)]
    for row in array_2d:
        print("".join([f"{element:>{width}}  " for element, width in zip(row, column_widths)]))
    print()
    return None

def solution(board):
    answer = 0
    n = len(board)
    distances = [[float("inf")]*n for _ in range(n)]
    distances[0][0] = 0
    
    ddx, ddy = [0, 0, -1, 1], [-1, 1, 0, 0]
    
    heap = []
    heapq.heappush(heap, (0, 0, 0, 's'))
    while heap:
        # print()
        # print(heap)
        x, y, cost, way = heapq.heappop(heap)
        # print('pop:', x, y, cost, way)
        for i in range(4):
            nx = x + ddx[i]
            ny = y + ddy[i]
            if 0<=nx<n and 0<=ny<n and board[ny][nx] != 1:
                if x == nx: # 상하
                    nway = 'd'
                elif y == ny: # 좌우
                    nway = 'f'
                    
                if way == 's':
                    ncost = cost+100
                else:
                    if way == nway:
                        ncost = cost+100
                    else:
                        ncost = cost+600
                
                if ncost <= distances[ny][nx]:
                    distances[ny][nx] = ncost
                    heapq.heappush(heap, (nx, ny, ncost, nway))
                    # print(nx, ny, ncost, nway)
        # printdis(distances)
    
    return distances[n-1][n-1]

# 분석: 다익스트라는 이러한 경우에서는 오류가 발생한다