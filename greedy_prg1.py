def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in lost:
        a = i
        b = i - 1
        c = i + 1
        if a in reserve:
            continue
        elif b in reserve and not(b in lost):
            reserve.remove(b)
        elif c in reserve and not(c in lost):
            reserve.remove(c)
        else:
            n -= 1
    return n
