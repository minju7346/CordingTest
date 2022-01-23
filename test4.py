import numpy as np


def solution(board, moves):
    answer = 0
    b_len = len(board[0])
    st = [-1]
    b_arr = np.zeros((b_len, 1))
    b_arr = b_arr.tolist()
    for i in range(b_len):
        for j in range(b_len):
            if board[b_len-1-j][i] != 0:
                b_arr[i].append(board[b_len-1-j][i])
    for i in moves:
        chk = b_arr[i-1].pop()
        if chk == 0:
            b_arr[i-1].append(0)
            continue
        elif chk == st[-1]:
            answer += 2
            st.pop()
            continue
        st.append(chk)
    return answer
