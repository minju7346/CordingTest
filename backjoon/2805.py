N, M = map(int, input().split())
trees = list(map(int, input().split()))

def binary(start, end):
    res = 0
    while start <= end:
        tot = 0
        mid = (start+end)//2
        for t in trees:
            if t > mid:
                tot += t-mid
        if tot >= M:
            res = max(res, mid)
            start = mid+1
        else:
            end = mid-1
    return res

print(binary(0,max(trees)))