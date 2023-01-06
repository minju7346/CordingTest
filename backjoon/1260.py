from collections import deque

N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]

for x, y in arr:
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

def dfs(v):
    if visited[v] == 0:
        visited[v] = 1
        print(v, end=' ')
        for i in graph[v]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        if visited[cur] == 0:
            visited[cur] = 1
            print(cur, end=' ')
            graph[cur].sort()
            for i in graph[cur]:
                q.append(i)

visited = [0]*(N+1)
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)

