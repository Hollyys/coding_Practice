def move(dir, dist, n, cursor, answer):
    if dir == 'U':
        for i in range(dist):
            cursor -= 1
            if cursor == 0:
                break
            if answer[cursor] == 'X':
                cursor -= 1
            if cursor == 0:
                break
    else:
        for i in range(dist):
            cursor += 1
            if cursor == n-1:
                break
            if answer[cursor] == 'X':
                cursor += 1
            if cursor == n-1:
                break
    return cursor

def name(index):
    if index == 0:
        return '무지'
    elif index == 1:
        return '콘'
    elif index == 2:
        return '어피치'
    elif index == 3:
        return '제이지'
    elif index == 4:
        return '프로도'
    elif index == 5:
        return '네오'
    elif index == 6:
        return '튜브'
    else:
        return '라이언'

def solution(n, k, cmd):
    answer = 'O'*n
    deleted = []
    cursor = k

    for i in cmd:
        if i == 'C':
            answer = answer[:cursor]+'X'+answer[cursor+1:]
            deleted.append(cursor)
            if cursor == n-1:
                cursor -= 1
            else:
                cursor += 1
        elif i == 'Z':
            pop = deleted.pop()
            answer = answer[:pop]+'O'+answer[pop+1:]
        else:
            cursor = move(i[0], int(i[2]), n, cursor, answer)
        # print(i, '\t', name(cursor), '\t', answer, deleted)
    return answer