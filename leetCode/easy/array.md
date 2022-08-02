- ### 배열은 L, R인덱스를 잡아 조건을 확인하면서 이동시켜주는 방법이 가장 쉬움
    ##### while문으로 R < len(arr)조건을 잡아서 오버플로우가 나지 않도록 해줌
- ### 배열은 값이 변하는 성질인 mutable성질이기 때문에 array를 복사할때는 주소복사가 아닌 전체 복사가 필요
    ##### 일차원 배열을 복사할때는 nums[:] = a를 통해 주소를 바꾸는 것이 아닌 nums배열자체의 값을 바꾸는 방법을 사용
    ##### 이차원 배열에서는 복사할때 from copy import deepcopy에서 arr = deepcopy(matrix)를 통해 객체를 생성 복사해줌
- ### rotate와 같이 배열을 끝에서 앞으로 도는 형태일때는 오버플로우 방지를 위해 a[(i+k)%n]처럼 인덱스를 전체크기로 %연산해줌
- ### XOR연산인 ^비트연산은 같은 숫자를 했을때 0이됨 -> 겹치지 않는 숫자를 찾을 때 유용
- ### Counter객체를 통해 해당 배열에 같은 숫자가 겹치는 개수를 이용한 문제를 푸는데 적합
- ### for idx, value in enumerate(nums)를 통해서 배열의 인덱스와 값을 이용할 수 있음
    #####   _dict[target - value] = idx와 같이 딕셔너리를 이용해서 인덱스와 값을 같이 이용해야할때 사용
- ### 배열을 분면으로 나눌때는 인덱스를 길이만큼으로 나눠서 저장함 -> squares[(r //3, c //3)])
- 배열회전은 행과 열의 인덱스 규칙을 찾아서 인덱스로 바꿈 & deepcopy이용(일시저장 배열에 deepcopy로 저장해서 붙여넣기함)