n = int(input())
a_num = int(input())
a_list = []
for i in range(a_num):
    tmp = list(map(int, input().split()))
    a_list.append(tuple(tmp))
d_num = int(input())
d_list = []
for i in range(d_num):
    tmp = list(input().split())
    d_list.append(tuple(tmp))
status = ["e","s","w",'n']
my_status = 0
dummy = [(1,1)]
t,i,j = 0,1,1
while True:
    t += 1
    t_i, t_j = i, j
    if status[my_status] == "e":
        j+=1
        if j > n :
            break
    elif status[my_status] == "s":
        i+=1
        if i > n :
            break
    elif status[my_status] == "w":
        j-=1
        if j < 1 :
            break
    elif status[my_status] == "n":
        i-=1
        if i < 1 :
            break
    if (i,j) in dummy:
        break
    dummy.append((i, j))
    if (i,j) not in a_list:
        dummy.pop(0)
    else:
        a_list.remove((i,j))
    if (str(t),"L") in d_list:
        my_status -= 1
        if my_status == -1:
            my_status = 3
    elif(str(t),"D") in d_list:
        my_status += 1
        if my_status == 4:
            my_status = 0

print(t)