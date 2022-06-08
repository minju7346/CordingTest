istr = input()
a = ''
tot = 0
k = 1
for i in istr:
    if (i >= '0' and i <= '9'):
        a += i
        continue
    tot += int(a) * k
    a = ''
    if i == '-':
        k = -1
tot += int(a) * k
print(tot)