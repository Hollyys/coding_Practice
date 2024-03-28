def solution(n, words):
    log = []
    idx = 0
    last_alpha = words[0][0]

    for word in words:
        if word in log or word[0] != last_alpha:
            return [idx%n+1, idx//n+1]
        else:
            log.append(word)
            last_alpha = word[-1]
            idx += 1

    return [0,0]