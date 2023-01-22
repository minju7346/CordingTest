import math
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

def binary(start, end, target):
    result = math.inf
    while start <= end:
        mid = (start+end)//2
        tot = 0
        for i in range(N):
            tot += mid//arr[i]
        if tot >= target:
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

arr.sort()
print(binary(1, arr[0]*M, M))