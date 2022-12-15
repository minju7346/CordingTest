N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
arr2 = []
for idx, num in enumerate(arr):
    arr2.append(num*(N-idx))
print(max(arr2))