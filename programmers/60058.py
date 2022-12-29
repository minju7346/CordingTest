def solution(p):
    if right(p):
        return p
    if not p:
        return ""
    u, v = "", ""
    for idx, i in enumerate(p):
        u += i
        if u.count('(') == u.count(')'):
            v = p[idx+1:]
            break
    if right(u):
        return u + solution(v)
    else:
        new_u = '(' + solution(v) + ')'
        u = u[1:-1]
        new_u += u[::-1]
    return new_u

def right(s):
    stack = []
    for i in s:
        if stack:
            if stack[-1]+i == "()":
                stack.pop()
                continue
        stack.append(i)
    if stack:
        return False
    else:
        return True

print(solution("()))((()"))