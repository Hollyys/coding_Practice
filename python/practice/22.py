def solution(record):
    answer = []
    dict = {}
    
    for d in record:
        data = d.split()
        if data[0] != 'Leave':
            dict[data[1]] = data[2]

    for d in record:
        data = d.split()
        if data[0] == 'Enter':
            msg = dict[data[1]]+"님이 들어왔습니다."
            answer.append(msg)
        elif data[0] == 'Leave':
            msg = dict[data[1]]+"님이 나갔습니다."
            answer.append(msg)
        
    return answer