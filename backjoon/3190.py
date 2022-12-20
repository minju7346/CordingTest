from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
turns = [list(input().split()) for _ in range(L)]
sec = 0
body = deque([[1, 1]])
row, col = 1, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
while True:
    sec += 1
    row += dx[d]
    col += dy[d]
    if 1 > row or row > N or 1 > col or col > N:
        break
    if [row, col] in body:
        break
    body.appendleft([row, col])
    if [row, col] in apples:
        apples.remove([row, col])
    else:
        body.pop()

    if [str(sec), 'L'] in turns:
        d -= 1
        if d < 0:
            d += 4
    elif [str(sec), 'D'] in turns:
        d += 1
        if d > 3:
            d -= 4
print(sec)

