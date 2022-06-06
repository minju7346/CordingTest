def dfs(graph, v, visited=[]):
    visited.append(v)
    print(v, end=' ') #방문등록

    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited) #해당 노드의 연결된 노드들을 하나씩 다 재귀함수에 끝까지 넣어줌

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

visited = []

dfs(graph, 1)