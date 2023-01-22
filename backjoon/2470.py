import math

def binary(start, end, idx):
    result = [math.inf, 0, 0]
    while start <= end:
        mid = (start+end)//2
        tot = arr[idx]+arr[mid]
        if abs(tot) < result[0]:
            result = [abs(tot), idx, mid]
        if tot > 0:
            end = mid - 1
        else:
            start = mid + 1
    return result

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = math.inf
ans1, ans2 = 0, 0
answer = []
for i in range(N):
    res, a, b = binary(0, N-1, i)
    if res < ans and a != b:
        ans1, ans2 = a, b
        ans = res

if arr[ans1] > arr[ans2]:
    ans1, ans2 = ans2, ans1
print(arr[ans1],arr[ans2])