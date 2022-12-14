N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum, pre = 0, 0
for i in arr:
    sum += pre + i
    pre = pre + i
print(sum)