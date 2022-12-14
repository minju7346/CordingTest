num, k = map(int, input().split())
arr = [int(input()) for _ in range(num)]
arr.sort(reverse=True)

sum = 0
for i in arr:
    if k // i != 0:
        sum += k // i
        k -= (k//i)*i
print(sum)