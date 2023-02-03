N = int(input())
arr = list(map(int, input().split()))

dp = arr[:]
print(dp)
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]

print(max(dp))