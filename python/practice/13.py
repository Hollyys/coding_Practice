def solution(board, moves):
    answer = 0
    n = len(board)
    stacks = [[] for _ in range(n)]
    stack = []
    for i in range(n):
        for j in range(n):
            if board[j][i] != 0:
                stacks[i].append(board[j][i])
        stacks[i] = stacks[i][::-1]
    
    for i in moves:
        if not stacks[i-1]:
            continue
        pop = stacks[i-1].pop()
        if stack and pop == stack[-1]:
            answer += 2
            stack.pop()
        else:
            stack.append(pop)
            
    return answer