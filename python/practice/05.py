def solution(arr1, arr2):
    answer = 0

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for k in range(len(arr2)):
                answer += arr1[i][j] * arr2[k][j]
                
    return answer

print(solution([[1,4],[3,2],[4,1]],[[3,3],[3,3]]))