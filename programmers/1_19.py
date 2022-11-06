def solution(n, k, cmd):
    cur = k
    answer = ['O'] * n
    table = {i:[i-1, i+1] for i in range(n)} # 링리를 딕셔너리로 구현하여 시간 더 줄임
    table[0], table[n-1] = [None, 1], [n-2, None] #맨 앞뒤 수정
    stack = []
    for c in cmd:
        if c == 'C': # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            #커서옮기기
            if next == None: # 맨 끝이면 커서를 전걸로 옮김
                cur = table[cur][0]
            else: # 맨 끝이 아니라면 커서를 다음걸로 옮기
                cur = table[cur][1]
            #삭제노드가 맨끝이거나 앞일때 특수케이스 업뎃
            if prev == None: # 맨앞이면 그 앞요소의 전노드를 None으로
                table[next][0] = None
            elif next == None: # 맨끝이면  그 전요소의 다음노드 None으로
                table[prev][1] = None
            else: # 맨 끝이나 맨 앞이 아닌경우 업뎃
                table[prev][1] = next
                table[next][0] = prev

        elif c == 'Z': # 복구
            prev, cal, next = stack.pop()
            answer[cal] = 'O'
            if prev == None:
                table[next][0] = cal
            elif next == None:
                table[prev][1] = cal
            else:
                table[next][0] = cal
                table[next][1] = cal
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)

print(solution(8,2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))