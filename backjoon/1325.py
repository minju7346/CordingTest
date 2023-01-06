from collections import deque
N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
cnt = [0]*(N+1)
result = []
for x, y in g:
    graph[y].append(x)
def bfs(v):
    tot = 0
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        if visited[cur] == 0:
            tot += 1
            visited[cur] = 1
            for j in graph[cur]:
                q.append(j)
    return tot

for i in range(1,N+1):
    visited = [0]*(N+1)
    cnt[i] = bfs(i)

mnum = max(cnt)
for idx, i in enumerate(cnt):
    if i == mnum:
        result.append(idx)
result.sort()
for i in result:
    print(i, end=' ')