from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())
sec, pre = 0, 0

q = deque()
for num in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == num:
                q.append((i,j))
ql = len(q)
while q:
    x, y = q.popleft()
    if pre != maps[x][y]:
        sec += 1
    if sec//ql == S:
        break
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<n and 0<=ty<n:
            if maps[tx][ty] == 0:
                maps[tx][ty] = maps[x][y]
                q.append((tx, ty))
print(maps[X-1][Y-1])