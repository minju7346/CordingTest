C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [1000000]*C

for i in range(C):
    for pay, num in arr:
        if i-num < 0:
            dp[i] = min(pay, dp[i])
        else:
            dp[i] = min(dp[i-num]+pay, dp[i])
print(dp[C-1])