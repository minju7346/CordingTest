dartResult ="1D2S#10S"
result = [0]
i=0
for i in range(len(dartResult)):
    print(i,result,dartResult[i])
    if dartResult[i].isdigit():
        result.append(result.pop()*10+int(dartResult[i]))
    elif dartResult[i] == 'S':
        result.append(0)
    elif dartResult[i] == 'D':
        result[-1] **= 2
        result.append(0)
    elif dartResult[i] == 'T':
        result[-1] **= 3
        result.append(0)
    elif dartResult[i] == "*":
        if i-3 >= 0:
            result[-3] *= 2
        result[-2] *= 2
    else:
        result[-2] *= -1
    i += 1
print(result)