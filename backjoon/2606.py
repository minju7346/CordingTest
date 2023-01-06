from collections import deque

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for x, y in arr:
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(N+1)
visited[1] = 1
cnt = 0
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for c in graph[cur]:
        if visited[c] == 0:
            cnt += 1
            visited[c] = 1
            q.append(c)
print(cnt)