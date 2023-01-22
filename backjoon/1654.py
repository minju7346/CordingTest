def binary(start, end):
    res = 0
    while start <= end:
        tot = 0
        mid = (start+end)//2
        for l in lines:
            tot += l//mid
        if tot >= N:
            res = max(res, mid)
            start = mid + 1
        else:
            end = mid - 1
    return res

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
print(binary(1, max(lines)))
