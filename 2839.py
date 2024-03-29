N = int(input())
dp = [5000]*(N+2)
dp[3] = 1
if N > 4:
    dp[5] = 1
for i in range(3, N+1):
    if i-5 >= 0:
        dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)
    else:
        dp[i] = min(dp[i], dp[i-3]+1)
if dp[N] == 5000:
    print(-1)
else:
    print(dp[N])
