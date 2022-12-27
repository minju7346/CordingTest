from collections import deque

def bfs(x):
    q = deque([x])
    while q:
        v = q.popleft()
        for i in arr[v]:
            if glen[i] == -1:
                q.append(i)
                glen[i] = glen[v] + 1

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
glen = [-1] * (N + 1)
glen[X] = 0
bfs(X)
for idx, i in enumerate(glen):
    if i == K:
        print(idx)
if K not in glen:
    print(-1)
