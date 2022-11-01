#orders의 원소를 하나씩 돌면서 해당 문자열 원소에서 k개의 조합을 찾음
#해당 조합 문자열 붙혀서 집합에 넣고 리조트 리스트에 추가
#k를(조건으로 k보다 작으면 안뽑음) 다 돌면서 끝나면 카운터를 이용해서
#가장 많이 나온 조합들 순으로 정렬 후 리턴
#k는 course에서 빼서 돌림

from itertools import combinations
from collections import Counter
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
answer = []
for k in course:
    tmp_set = []
    for order in orders:
        for com in combinations(order, k):
            res = ''.join(sorted(com))
            tmp_set.append(res)
    sorted_set = Counter(tmp_set).most_common()
    answer += [menu for menu, cnt in sorted_set if cnt > 1 and cnt == sorted_set[0][1]]
print(sorted(answer))


