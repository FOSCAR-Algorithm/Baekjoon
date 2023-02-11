# 로또
# https://www.acmicpc.net/problem/6603

# 조합 (Combinaton)
from itertools import combinations

while True:
    array = list(map(int, input().split()))

    # array로 한번에 입력 받아서 0번째 인덱스 값을 k, 1~ 인덱스 값을 temp_s list로 구분
    k = array[0] 

    # k == 0 일 때 While문 벗어나면서 종료
    if k == 0:
        break
    
    temp_s = array[1:]

    # combinations 함수 이용하여 temp_s의 인자값들의 조합을 S list에 담음 (S는 2차원 list)
    S = combinations(temp_s, 6)

    # 출력
    for i in S:
        for j in i:
            print(j, end=' ')
        print()
    print()