s = input()
flag = 1
sum = 0
tmp = ''
for i in s:
    if '0' <= i <= '9':
        tmp += i
        continue
    sum += int(tmp) * flag
    tmp = ''
    if i == '-':
        flag = -1

sum += int(tmp)*flag
print(sum)