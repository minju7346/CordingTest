num = int(input())
narr = [list(map(int,input().split())) for _ in range(num)]
narr.sort(key=lambda x: (x[1],x[0]))
start = 0
tot = 0
for i, j in narr:
    if start <= i:
        start = j
        tot += 1
print(tot)