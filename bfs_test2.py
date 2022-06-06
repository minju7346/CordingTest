from collections import deque

def bfs(graph, start):
    queue = deque([start]) #방문할 노드를 넣어두는 곳
    visited = [] #방문한 노드들

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        if v not in visited:
            visited.append(v)
            queue += graph[v]

    return visited

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

print(bfs(graph, 1))
