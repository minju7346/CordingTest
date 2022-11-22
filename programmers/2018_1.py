def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
        maps.append(
            bin(arr1[i]|arr2[i])[2:] # OR연산후 이진수로 변환, 앞에 '0b'부분 슬라이싱하여 순수 숫자만 출력
                .zfill(n) # 남은 n개의 공간 앞을 0으로 채움
                .replace('1', '#')
                .replace('0', ' ')
        )
    return maps