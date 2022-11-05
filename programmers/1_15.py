def solution(places):
    answer = []

    for room in places:
        print(room)
        p_position = []
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    p_position.append([i, j])
        if check(p_position, room):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def check(p_position, room):
    for i in range(len(p_position)):
        for j in range(i+1, len(p_position)):
            f = p_position[i]
            b = p_position[j]
            m_len = abs(f[0] - b[0]) + abs(f[1] - b[1])
            if m_len == 1:
                return False
            elif m_len == 2:
                if f[0] == b[0]:
                    if room[f[0], f[1]+1] != 'X':
                        return False
                elif f[1] == b[1]:
                    if room[f[0]+1, f[1]] != 'X':
                        return False
                elif not room[f[0], b[1]] != 'X' and room[b[0], f[1]] != 'X':
                    return False
    return True