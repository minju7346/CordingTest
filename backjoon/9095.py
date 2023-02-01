T = int(input())

while T > 0:
    T-= 1
    n = int(input())
    dp = [1e9]*(n+1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    if n > 2:
        dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])