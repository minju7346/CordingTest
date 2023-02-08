n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n):
    day, pay = arr[i][0], arr[i][1]
    if dp[i] < dp[i-1]: # 전날 일을 하지 않았을떄
        dp[i] = dp[i-1]
    if i+day < n+1 and dp[i+day] < pay+dp[i]:
        dp[i+day] = pay+dp[i]
print(max(dp))