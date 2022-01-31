a = list(map(int, input()))
b = len(a)//2
if sum(a[:b]) == sum(a[b:]):
    print("LUCKY")
else:
    print("READY")
