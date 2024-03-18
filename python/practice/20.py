def solution(participant, completion):
    dic = {}
    for c in completion:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
            
    for p in participant:
        if not p in dic or dic[p] < 1:
            return p
        else:
            dic[p] -= 1