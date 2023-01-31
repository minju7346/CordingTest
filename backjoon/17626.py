import math
n = int(input())
cnt = 0
while n > 0:
    print(n, math.sqrt(n), int(math.sqrt(n)))
    n -= int(math.sqrt(n))*int(math.sqrt(n))
    cnt += 1
print(cnt)