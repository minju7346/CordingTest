import math
n = int(input())
dp =[1e9]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp,dp[n])
