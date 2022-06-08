num = int(input())
aarr = list(map(int, input().split()))
barr = list(map(int, input().split()))
aarr.sort()
barr.sort(reverse=True)
sum = 0
for i in range(num):
    sum += aarr[i] * barr[i]
print(sum)