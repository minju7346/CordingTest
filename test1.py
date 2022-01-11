def solution(lottos, win_nums):
    num1 = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    num2 = len(lottos & win_nums)
    min = 6 - (num2 - 1)
    if min == 7:
        min = 6
    max = min - num1 + 1
    if (max == 6) & (num1 < 2):
        max = 6
    answer = [min, max]
    return answer
