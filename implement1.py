n = 5
a, b, c = 0, 0, 0
sum = 0
while not(a == n and b == 59 and c == 59):
    c += 1
    if c == 60:
        c = 0
        b += 1
        if b == 60:
            b = 0
            a += 1
    if '3' in str(a)+str(b)+str(c):
        sum += 1
print(sum)
