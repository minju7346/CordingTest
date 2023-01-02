from itertools import combinations
import copy

N = int(input())
maps = [list(input().split()) for _ in range(N)]
empty = []
teacher = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(xx, yy, d):
    global flag
    tx = xx + dx[d]
    ty = yy + dy[d]
    if 0 <= tx < N and 0 <= ty < N:
        if tmp[tx][ty] == 'S':
            flag = 1
        elif tmp[tx][ty] == 'X':
            dfs(tx, ty, d)


for i in range(N):
    for j in range(N):
        if maps[i][j] == 'X':
            empty.append([i, j])
        elif maps[i][j] == 'T':
            teacher.append([i, j])

for emp in combinations(empty, 3):
    tmp = copy.deepcopy(maps)
    flag = 0
    for x, y in emp:
        tmp[x][y] = 'O'
    for x, y in teacher:
        for i in range(4):
            dfs(x, y, i)
    if flag == 0:
        print("YES")
        exit(0)
print('NO')
