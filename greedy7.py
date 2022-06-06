onum = int(input())
res = 5000
a = 0
while 3 * a <= onum:
    num = onum
    num -= 3*a
    b = num // 5
    if num - 5*b == 0:
        if res > a+b:
            res = a+b
    elif num == 0:
        if res > a+b:
            res = a+b
    a += 1
if res != 5000:
    print(res)
else:
    print(-1)