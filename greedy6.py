n, m = 5, 3
arr = [1, 1, 1, 2, 3]
sum = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] != arr[j]:
            sum += 1
print(sum)
