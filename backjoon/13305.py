N = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

sum, td, pre_p = 0, 0, price[0]
for d, p in zip(dis, price[1:]):
    if pre_p > p:
        sum += (td+d)*pre_p
        pre_p = p
        td = 0
    else:
        td += d
if td != 0:
    sum += td*pre_p
print(sum)
