num = input()
result = 0
a = ord(num[0])-96
b = int(num[1:])
if (a - 1) > 0 and (b - 2) > 0:
    result += 1
if (a - 2) > 0 and (b - 1) > 0:
    result += 1
if (a + 1) < 8 and (b - 2) > 0:
    result += 1
if (a + 2) < 8 and (b - 1) > 0:
    result += 1
if (a + 2) < 8 and (b + 1) < 8:
    result += 1
if (a + 1) < 8 and (b + 2) < 8:
    result += 1
if (a - 2) > 0 and (b + 1) < 8:
    result += 1
if (a - 1) > 0 and (b + 2) < 8:
    result += 1
print(result)
