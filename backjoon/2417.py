n = int(input())
result =  2**63 +1
def binary(start, end):
    global  result
    while start <= end:
        mid = (start + end) // 2
        if mid*mid >= n:
            result = min(mid, result)
            end = mid-1
        elif mid*mid < n:
            start = mid+1
        else:
            end = mid-1
binary(0, n)
print(result)