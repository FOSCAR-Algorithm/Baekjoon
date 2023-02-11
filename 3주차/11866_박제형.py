# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

from collections import deque

N, K = map(int,input().split())

deque = deque()
result = []

[deque.append(i) for i in range(1, N+1)] # 1부터 N까지 deque에 append

while deque: # deque에 원소가 있으면 반복  
    for _ in range(K-1): # K-1만큼 반복(K번째에는 지우면서 result 삽입하기 위해서 따로 처리)
        deque.append(deque.popleft()) # 왼쪽 원소 두개 지우면서 동시에 맨 뒤로 삽입
    result.append(deque.popleft()) # 세번 째 원소 지우면서 result list에 삽입


print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>')




# for i in range(1, N+1):
#     index = (i*K) % N
#     temp = list[index-1]
#     print(temp, end=' ')
#     list.remove(temp)