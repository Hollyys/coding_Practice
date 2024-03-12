def solution(dirs):
    answer = 0
    curr_x = 0
    curr_y = 0
    log = {}
    
    for dir in dirs:
        start_key = str(curr_x) + str(curr_y)
        if dir == 'U':
            curr_y += 1
            if curr_y > 5:
                curr_y -= 1
        elif dir == 'D':
            curr_y -= 1
            if curr_y < -5:
                curr_y += 1
        elif dir == 'R':
            curr_x += 1
            if curr_x > 5:
                curr_x -= 1
        else:
            curr_x -= 1
            if curr_x < -5:
                curr_x += 1
        
        curr_key = str(curr_x) + str(curr_y)
        key = start_key + curr_key
        if not key in log and start_key != curr_key:
            log[start_key + curr_key] = True
            log[curr_key + start_key] = True
            answer += 1
    return answer