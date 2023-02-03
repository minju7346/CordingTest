#초기화를 1로 해야함, 초기화 항상 생각해서 할 것
N = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dp = [1]*(N+1)
for i in range(2, N+1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
