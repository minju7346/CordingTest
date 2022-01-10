def solution(lottos, win_nums):
    lottos = set(lottos)
    win_nums = set(win_nums)
    num = len(lottos&win_nums)
    a = 6 - (num -1)
    if a == 7:
        a = 6
    elif a == 6:
        
    b = a + 2 
    
    answer = [a, b]
    return answer

