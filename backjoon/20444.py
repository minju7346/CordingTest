def binary(start, end, target):
    while start <= end:
        mid = (start+end)//2
        tot = (mid+1)*(n-mid+1)
        if tot < k:
            end = mid - 1
        elif tot > k:
            start = mid + 1
        else:
            return "YES"
    return "NO"

n, k = map(int, input().split())
print(binary(0, n, k))