import math
def binary(start, end):
    res = math.inf
    while start <= end:
        mid = (start+end)//2
        bef = 0
        for idx, a in enumerate(arr):
            if ((idx+1)-(bef+1))*(1+abs(arr[idx]-arr[bef])) <= mid:
                bef = idx
        if bef == len(arr)-1:
            res = min(res, mid)
            end = mid - 1
        else:
            start = mid + 1
    return res

N = int(input())
arr = list(map(int, input().split()))
print(binary(1, max(arr)))