x = "5525"
y = "1255"
tmp = []
answer =''
for i in x:
    if i in y:
        tmp.append(i)
        y = y.replace(i,'',1)
        print(i,y)
tmp.sort(reverse=True)
for i in tmp:
    answer+=i
print(int(answer)