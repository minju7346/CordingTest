n, m = 2, 4
arr = [[7, 3, 1, 8], [3, 3, 3, 4]]
big = 0
idx = 0
for i in range(n):
    if big < min(arr[i]):
        big = min(arr[i])
        idx = i
print(min(arr[idx]))
