def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False
n, m = map(int, input().split())
#n, m 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
#graph 입력받기

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)

#하나의 노드를 잡고 끝날 떄 까지 계속 들어감 -> 깊이 우선 탐색


