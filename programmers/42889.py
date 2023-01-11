from collections import Counter
def solution(N, stages):
    tot = len(stages)
    ans = list(Counter(stages).items())
    ans.sort()
    result = [[0, i] for i in range(1, N+2)]
    for idx, num in ans:
        result[idx-1] = [num/tot,idx]
        tot -= num
    if result[N-1] == [0, N]: result[N-1] = [0, N]
    result = result[:-1]
    result.sort(reverse=True, key=lambda x:(x[0]))
    answer = []
    for i in result
        answer.append(i[1])
    return answer

print(solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3]))