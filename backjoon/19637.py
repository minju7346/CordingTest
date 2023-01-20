import math
N, M = map(int, input().split())
state = {}
maxn = 0

def binary(start, end, target):
    res = math.inf
    while start <= end:
        mid = (start+end)//2
        if state[mid][0] >= target:
            end = mid-1
            res = min(mid,res)
        else:
            start = mid+1
    return state[res][1]

for _ in range(N):
    a = input().split()
    maxn = max(maxn, len(a[1]))
    if int(a[1]) not in state:
        state[int(a[1])]=a[0]
state = list(state.items())
number = [int(input()) for _ in range(M)]
for num in number:
    print(binary(0, len(state), num))
