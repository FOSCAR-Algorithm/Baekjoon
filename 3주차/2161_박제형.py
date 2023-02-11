# 카드 1
# https://www.acmicpc.net/problem/2161

# deque 사용
from collections import deque

n = int(input())

deque = deque() 

for i in range(1, n+1): # 왼쪽이 위, 오른쪽이 아래로 가정 ex. [1, 2, 3, 4, 5]
    deque.append(i)

# print(len(deque))

while(True):
    if len(deque) == 1: # 1개의 카드만 남게 되면 해당 카드 print후 break로 반복문 탈출
        print(deque.pop())
        break

    print(deque.popleft(), end=" ")
    deque.append(deque.popleft()) # 제일 아래에 다음 젤 위에 카드(지우면서) 삽입