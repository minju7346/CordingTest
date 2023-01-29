#최대 증가 수열은 각 인덱스를 돌면서 최대 몇번쨰로 큰지 앞에 있는 값들을
#돌면서 갱신해 나가는 형태로 반대로 주어진경우 reverse를 사용
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1]*(n+1)

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))