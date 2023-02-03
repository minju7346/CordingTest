n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dp = [-1e9]*(n+1)
dp[1] = arr[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1]+arr[i], arr[i-1]+arr[i], arr[i])
print(max(dp))