money = int(input())
stock = list(map(int, input().split()))
jun_m, sung_m = money, money
jun_s, sung_s =0, 0
three = 0
pre = stock[0]
for i in stock:
    tmp = 0
    if i <= jun_m:
        tmp = jun_m // i
        jun_s += tmp
        jun_m -= (tmp*i)
    if pre < i:
        if three < 0:
            three = 0
        three += 1
    elif pre > i:
        if three > 0:
            three = 0
        three -= 1
    else:
        three = 0
    if three <= -3:
        tmp = sung_m // i
        sung_s += tmp
        sung_m -= (tmp*i)
    elif three >= 3:
        sung_m += sung_s*i
        sung_s = 0
    pre = i
jun_m += jun_s * stock[-1]
sung_m += sung_s*stock[-1]
if jun_m>sung_m:
    print('BNP')
elif jun_m<sung_m:
    print('TIMING')
else:
    print('SAMESAME')