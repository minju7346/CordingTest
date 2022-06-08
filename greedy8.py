num, k = map(int, input().split())
arr = [int(input()) for _ in range(10)]
arr.sort(reverse=True)
sum = 0
for i in arr:
    if k == 0:
        break
    if k // i != 0:
        a = k//i
        sum += a
        k -= a*i
print(sum)