N = int(input())
arr = list(map(int, input().split()))
m = int(input())
result = 0
def binary(start, end):
    global result
    while start <= end:
        tot = 0
        mid = (start+end)//2
        for i in arr:
            if i>mid:
                tot += mid
            else:
                tot += i
        if tot > m:
            end = mid - 1
        else:
            start = mid + 1
            result = max(mid, result)
binary(0, max(arr))
print(result)