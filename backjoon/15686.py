from itertools import combinations

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
houses = []
chicks = []
for i, a in enumerate(arr):
    for j, num in enumerate(a):
        if num == 1:
            houses.append([i, j])
        elif num == 2:
            chicks.append([i, j])
tot = 100000000

for m_chi in list(combinations(chicks,M)):
    sum = 0
    for hx, hy in houses:
        hsum = 10000
        for cx, cy in m_chi:
            hsum = min(hsum, (abs(hx-cx)+abs(hy-cy)))
        sum += hsum
    tot = min(tot,sum)
print(tot)

