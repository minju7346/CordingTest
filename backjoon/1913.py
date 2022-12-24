dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
find = int(input())
arr = [[0]*N for _ in range(N)]
d, cnt, k, two  = 0, 0, 1, 0
x, y = N//2, N//2
arr[x][y] = 1
for i in range(2, N*N+1):
    x = x + dx[d]
    y = y + dy[d]
    arr[x][y] = i
    cnt += 1
    if cnt == k:
        cnt = 0
        two += 1
        d += 1
        if d > 3:
            d -= 4
    if two == 2:
        k += 1
        two = 0

for idx, i in enumerate(arr):
    for jdx, j in enumerate(i):
        print(j, end=' ')
        if j == find:
            x, y = idx, jdx
    print()
print(x+1, y+1)