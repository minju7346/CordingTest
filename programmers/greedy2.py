#큰수 만들기
number = '4321'
k=1
result = len(number)
stack = [number[0]]
for i in range(1, len(number)):
    while stack and int(stack[-1]) < int(number[i]) and k != 0:
        stack.pop()
        k -= 1
    stack.append(number[i])
if k != 0:
    print(number[:-k])

print(''.join(stack)+''.join(number[result:]))
