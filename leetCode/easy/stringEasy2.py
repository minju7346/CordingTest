x = 1534236469
print(2**31,x)
if x < -(2**31) or x >= 2**31-1:
    print(0)
    exit(0)
s = ''
flag = 1
if x < 0:
    flag = -1
    x *= -1
xstr = str(x)
xlen = len(xstr)
for i in range(xlen):
    s += xstr[xlen-1-i]
s = int(s)
s *= flag
print(int(s))