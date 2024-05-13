# 실패
def solution(numbers):
    answer = ''
    strings = []
    dict = {}
    
    for number in numbers:
        strings.append(str(number))
    strings.sort(key=lambda x: x[0], reverse = True)
    
    for string in strings:
        if string[0] in dict:
            dict[string[0]].append(int(string))
        else:
            dict[string[0]] = [int(string)]
    
    return answer

# 답안 일부 수정
import functools

def compare(a, b):
    t1 = str(a) + str(b)
    t2 = str(b) + str(a)

    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    answer = ""
    sorted_nums = sorted(numbers,
                         key=functools.cmp_to_key(compare), reverse=True)
    for x in sorted_nums:
        answer += str(x)
    return "0" if int(answer) == 0 else answer
# functools.cmp_to_key 함수를 이용하여 두 숫자를 함쳐서 만든 수의 크기를 비교하여
# 더 큰 쪽을 순서로 하여 정렬함
# 그냥 복잡하게 생각하지 말고 어떻게 조합하든
# 두 숫자를 붙여 만든 수가 더 크게끔 정렬한 것임.