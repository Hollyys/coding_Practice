from itertools import combinations_with_replacement
from collections import Counter

def score_gap(info, combi):
    score1, score2 = 0, 0
    for idx in range(11):
        if info[idx] < combi.count(10-idx):
            score1 += 10-idx
        elif info[idx] > 0:
            score2 += 10-idx
    return score1, score2

def calculate_score(info, combi):
    score1, score2 = 0, 0
    for i in range(1, 11):
        if info[10 - i] < combi.count(i):
            score1 += i
        elif info[10 - i] > 0:
            score2 += i
    return score1, score2

def solution(n, info):
    maxdiff, max_comb = 0, {}
    
    for combi in combinations_with_replacement(range(11), n):
        cnt = Counter(combi)
        score1, score2 = score_gap(info, combi)
        diff = score1 - score2
        if diff > maxdiff:
            max_comb = cnt
            maxdiff = diff
        
    if maxdiff > 0:
        answer = [0] * 11
        for n in max_comb:
            answer[10-n] = max_comb[n]
        return answer
    else:
        return [-1]