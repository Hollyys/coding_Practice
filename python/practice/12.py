def solution(prices):
    answer = []
    
    for index, price in enumerate(prices):
        cnt = 0
        for i in range(index+1, len(prices)):
            cnt += 1
            if prices[i] < price:
                break
        answer.append(cnt)
    return answer