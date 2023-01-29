N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0,0])
dp = [0]*(N+1)
if arr[1][0] <= N:
    dp[1] = arr[1][1]

for i in range(2, N+1):
    if (N + 1) - i < arr[i][0]:
        continue
    else:
        dp[i] = arr[i][1]
    for j in range(1, i):
        if i-j >= arr[j][0]:
            dp[i] = max(dp[i], dp[j]+arr[i][1])
print(max(dp))