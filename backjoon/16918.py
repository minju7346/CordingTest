import copy
R, C, N = map(int, input().split())
maps = [list(input()) for _ in range(R)]
maps1 = []
maps2 = []
maps3 = []
maps3 = copy.deepcopy(maps)
boom = [[] for i in range(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, o):
    maps[x][y] = '.'
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<R and 0<=ty<C:
            maps[tx][ty] = '.'
            if (tx, ty) in boom[o]:
                boom[o].remove((tx, ty))

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'O':
            boom[0].append((i, j))
time = 1
b = 1
for k in range(4):
    if (time%2) == 1:
        for i in range(R):
            for j in range(C):
                if maps[i][j] == '.':
                    maps[i][j] = 'O'
                    boom[b].append((i, j))
        b += 1
        if b == 2:
            b = 0
    else:
        if b == 0:
            o = 1
        else:
            o = 0
        while boom[b]:
            x, y = boom[b].pop()
            dfs(x, y, o)
    time += 1
    if k == 1:
        maps1 = copy.deepcopy(maps)
    elif k == 3:
        maps2 = copy.deepcopy(maps)
if N == 1:
    for i in range(R):
        print(''.join(maps3[i]))
elif N%2 == 0:
    for i in range(R):
        print('O'*C)
else:
    N -= (N//4)*4
    if N == 3:
        for i in range(R):
            print(''.join(maps1[i]))
    else:
        for i in range(R):
            print(''.join(maps2[i]))