def solution(enroll, referral, seller, amount):
    answer = []
    parent = {}
    total = {}

    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]

    for i in range(len(enroll)):
        total[enroll[i]] = 0

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]
        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10

    for name in total:
        answer.append(total[name])

    return answer

maps = ["SOOOL", "OOOOO", "OOOOO", "OOOOO", "OOOOE"]
if not maps[-1][-1]:
    print('helo')