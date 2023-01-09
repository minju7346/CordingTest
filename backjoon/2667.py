from collections import deque

N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global tot
    if visited[x][y] == 0:
        visited[x][y] = 1
        tot += 1
        for d in range(4):
            tx = x+dx[d]
            ty = y+dy[d]
            if 0<=tx<N and 0<=ty<N and maps[tx][ty] == 1:
                dfs(tx, ty)
    return tot
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            tot = 0
            result.append(dfs(i, j))
print(cnt)
for r in sorted(result):
    print(r)

