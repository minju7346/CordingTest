N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N) for _ in range(N)]
k = arr[0][0]
if 0 <= k < N and dp:
    dp[k][0] = 1
if 0 <= k < N:
    dp[0][k] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] != 0 and (i+j != (N-1)*2):
            k = arr[i][j]
            if i+k<N:
                dp[i+k][j] += dp[i][j]
            if j+k<N:
                dp[i][j+k] += dp[i][j]
print(dp[N-1][N-1])