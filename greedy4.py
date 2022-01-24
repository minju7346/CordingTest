a = "0011010110"
org = a[0]
result = 0
for i in a:
    if org != i:
        result += 1
    org = i
print(result//2)
