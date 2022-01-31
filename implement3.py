n, m = map(int, input().split())
array = [[1] * (m+2) for _ in range(n+2)]
x, y, d = map(int, input().split())
for i in range(1, n+1):
    array[i][1:5] = list(map(int, input().split()))
darr = [[0, -1], [0, 1], [1, 0], [0, -1]]
result = 1
x += 1
y += 1
chk = 0
while True:
    t_x = x+darr[d][0]
    t_y = y+darr[d][1]
    if array[t_x][t_y] != 1:
        array[x][y] = 1
        x, y = t_x, t_y
        result += 1
        chk = 0
    else:
        d -= 1
        chk += 1
        if d == -1:
            d = 3
    if chk == 4:
        x -= 1
        if array[x][y] == 1:
            break
print(result)
