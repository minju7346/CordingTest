N = input()
cut = len(N)//2
sum = 0
for i in N[:cut]:
    sum += int(i)
for i in N[cut:]:
    sum -= int(i)
if sum == 0:
    print("LUCKY")
else:
    print("READY")