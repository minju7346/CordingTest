n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1

for coin in arr:
    for i in range(1, k+1):
        if i-coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])