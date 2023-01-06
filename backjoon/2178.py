from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b, 1))
    while q:
        x, y, d = q.popleft()
        if x == N - 1 and y == M - 1:
            return d
        if visited[x][y] == 0:
            visited[x][y] = 1
            for i in range(4):
                tx = x+dx[i]
                ty = y+dy[i]
                if 0<=tx<N and 0<=ty<M and maps[tx][ty] == 1:
                    q.append((tx, ty, d+1))

visited = [[0]*M for _ in range(N)]
print(bfs(0,0))