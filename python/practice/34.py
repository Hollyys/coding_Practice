def solution(nums):
    answer = 0
    n = len(nums)
    mons = set()
    for mon in nums:
        mons.add(mon)
    answer = min(n/2, len(mons))
    return answer