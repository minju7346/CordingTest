n = 5
arr = [2, 3, 1, 2, 2]
result = 0
i = 0
arr.sort(reverse=True)
while i < n:
    i += arr[i] - 1
    if i >= n:
        break
    result += 1
    i += 1
print(result)
