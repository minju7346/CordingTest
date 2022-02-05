def solution(clothes):
    answer = 1
    c_arr = []
    c_dict = {}
    for cloth in clothes:
        c_dict[cloth[1]] = []
    for cloth in clothes:
        c_dict[cloth[1]].append(cloth[0])
    for value in c_dict.values():
        answer *= len(value)+1
    return answer-1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))