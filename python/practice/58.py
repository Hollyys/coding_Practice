def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        tmp = []
        for index in range(i-1, j):
            tmp.append(array[index])
        tmp.sort()
        answer.append(tmp[k-1])
    return answer