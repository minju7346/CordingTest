N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
day = [0 for _ in range(366)]
tot = 0

for s, e in arr:
    for i in range(s, e+1):
        day[i] += 1

last = 0
h = 1
for i in day:
    if i == 0:
        if last != 0:
            tot += last*h
            last = 0
            h = 1
    else:
        last += 1
        h = max(h,i)
if last != 0:
    tot += last * h
    last = 0
    h = 1
print(tot)