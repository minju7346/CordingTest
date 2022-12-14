N = int(input())
five = N // 5
while five != -1:
    if (N-five*5) % 3 == 0:
        print(five+(N-five*5)//3)
        exit(-1)
    else:
        five -= 1
print(-1)