n = 5
arr = [3, 2, 1, 1, 9]
arr.sort()
idx = 0
for i in range(1, n+1):
    if i not in arr:
        idx = i
        break
print(sum(arr[:i])+1)
