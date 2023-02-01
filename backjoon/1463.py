n = int(input())
dp = [1e9]*(n+1)
if n == 1:
    print(0)
    exit(0)
dp[1], dp[2] = 0, 1
for i in range(3, n+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])