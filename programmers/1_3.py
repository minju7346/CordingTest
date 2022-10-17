stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
People = len(stages)
faillist = {} # 딕셔너리를 통해 리스트의 크기순을 출력할 때 이용
for i in range(1, N + 1):
    if People != 0:
        faillist[i] = stages.count(i) / People
        People -= stages.count(i)
    else:
        faillist[i] = 0
print(faillist)
return sorted(faillist, key=lambda x: faillist[x], reverse=True)
#딕셔너리는 정렬하면 keys만 남음, 정렬은 faillist[x]이므로 value로 정렬