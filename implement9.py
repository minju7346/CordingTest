n, m = map(int, input().split())
city = [[0] * n for _ in range(n)]
for i in range(n):
    city[i] = list(map(int,input().split()))
sum_2 = 0
set1 = set()
set2 = set()
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            set1.add((i,j))
        elif city[i][j] == 2:
            set2.add((i,j))
            sum_2 += city[i].count(2)
result = 0
if sum_2 == m: #모든 M을 고르는 경우
    while len(set1) != 0:
        home = set1.pop()
        tmp = []
        for ck in set2:
            tmp.append(abs(home[0]-ck[0])+abs(home[1]-ck[1]))
        result += min(tmp)
else: #전체 치킨집 중 N개만 고르는 경우
    from itertools import combinations
    choice_ck = list(combinations(set2, m))
    choice_sum = 0
    t_result = []
    for c_ck in choice_ck:
        t_sum = 0
        for home in set1:
            tmp = []
            for ck in c_ck:
                tmp.append(abs(home[0] - ck[0]) + abs(home[1] - ck[1]))
            t_sum += min(tmp)
        t_result.append(t_sum)
    result = min(t_result)

print(result)


