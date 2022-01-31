a = list(input())
alpa = []
sum = 0
for i in a:
    if i.isalpha():
        alpa.append(i)
    else:
        sum += int(i)
alpa.sort()
print(''.join(alpa), end="")
print(sum)
