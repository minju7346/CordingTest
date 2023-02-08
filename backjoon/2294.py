n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [1e9]*(k+1)
dp[0] = 0

for coin in arr:
    for i in range(k+1):
        if i-coin >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])