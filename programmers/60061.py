ans = []
def possible(x,y,a,ans):
    if a == 0: #기둥일때
        if y == 0 or [x-1,y,1] in ans or [x,y,1] in ans or [x,y-1,0] in ans:
            return True
    else: #보일때
        if [x,y-1,0] in ans or [x+1,y-1,0] in ans or ([x-1,y,1] in ans and [x+1,y,1] in ans):
            return True
    return False

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
for x, y, a, b in build_frame:
    if b == 1: #설치
        if possible(x,y,a,ans):
            ans.append([x,y,a])
    else: # 삭제
        rem = 0
        tmp = ans.copy()
        tmp.remove([x,y,a])
        for xx,yy,aa in tmp:
            if not possible(xx,yy,aa,tmp):
                rem = 1
        if rem == 0:
            #print(x,y,a)
            ans.remove([x,y,a])
ans.sort(key=lambda x:(x[0], x[1])


