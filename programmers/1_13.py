#먼저 리스트화 시킴
#문자를 찾아서 해당 앞뒤 인덱스 값을 가져와서 계산후
#문자리스트 while문을 통해서 모든 순열 돌기-> 하나의 문자잡고 해당 문자없을때 까지 계산
#해당 문자를 기준으로 왼쪽으로 이동하면서
#모든 수의 순열조합을 통해 계산하여서 max로 answer값을 갱신해감
#문자별로 우선순위 붙여주고 괄호 씌어서 하나씩 계산시작
#return할 때 절대값 씌우기

from itertools import permutations
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def solution(expression):
    ex_list = []
    stack = []
    result = []
    op_list = list(permutations(['+', '-', '*'], 3))

    tmp = ''
    for i in expression: #리스트로 변환하기
        if i != '+' and i != '-' and i != '*':
            tmp += i
        else:
            ex_list.append(int(tmp))
            ex_list.append(i)
            tmp = ''
    ex_list.append(int(tmp))

    for op in op_list: #각 조합을 돌면서 꺼냄
        tmp_list = ex_list.copy()
        for o in op: # 각 조합별 우선순위 높은 것 부터 차례대로 연산
            while tmp_list:
                tmp = tmp_list.pop(0)
                if tmp == o:
                    stack.append(operation(stack.pop(), tmp_list.pop(0), o))
                else:
                    stack.append(tmp)
            tmp_list = stack.copy()
            stack = []
        result.append(abs(int(tmp_list[0])))
    return max(result)
print(solution("50*6-3*2"))