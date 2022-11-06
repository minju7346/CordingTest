#왼쪽은 마이너스 오른쪽은 플러스로 카운터해서 양음수에 따라 성격유형 출력
def solution(survey, choices):
    answer = ''
    type = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    for sur, num in zip(survey, choices):
        if sur in type:
            type[sur] += (num-4)
        else:
            type[sur[1]+sur[0]] -= num-4
    for t, n in type.items():
        if n > 0:
            answer += t[1]
        elif  n < 0:
            answer += t[0]
        else:
            answer += min(t)
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))