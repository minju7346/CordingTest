from collections import deque

def bfs(graph, x, visited):
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if glen[i] == -1:
                queue.append(i)
                glen[i] = glen[v] + 1


n, m, k, x = map(int, input().split())
graph = [[] * m for _ in range(n+1)]
visited = [False] * (n + 1)
visited[0] = True
result = []
glen = [-1] * (n + 1)
glen[x] = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
bfs(graph, x, visited)
for i in range(1,n+1):
    if glen[i] == k:
        print(i)
if k not in glen:
    print(-1)


#각각의 모든 노드를 순차적으로 접근하기 떄문에 너비우선탐색기법 사용