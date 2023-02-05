# 햄버거 분배
# https://www.acmicpc.net/problem/19941

# 1. k만큼 떨어진 것부터 탐색해야 최대한 많이 먹을 수 있다.(왼쪽 K ~ 0탐색 -> 오른쪽 K ~ 0탐색) => X! (K가 큰 경우 상황이 달라짐)
# 2. 가장 왼쪽에 있는 햄버거 먼저 먹기 ===> 이럼 최대한으로 먹을 수 있다.


N, K = map(int, input().split())
seq = list(input()) # 문자열이 아닌 list로 받기 (문자열로 받으면 하나 단위로 수정 불가능)

cnt=0

for i in range(len(seq)):
    if seq[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0<=j<len(seq) and seq[j] == 'H': # index(j)의 범위를 여기서 조절해 주었음 -> range(min(0, i-K), max(N, i+K+1))와 같이 할 수 도 있음
                cnt += 1
                seq[j] = 'X' # 먹은 햄버거는 X로 변경
                break

print(cnt)



# N, K = map(int, input().split())
# seq = input()
# check_list = [0]*len(seq) # seq와 같은 크기의 list 생성하여, 햄버거를 먹을 경우 동일한 인덱스(0 -> 1)로 표시

# cnt=0

# for i in range(len(seq)):
#     if seq[i] == 'P':
#         # print('i :', i)
#         for j in range(i-K, i+K+1): # K-- (1까지)
#             if i-j >= 0 and seq[i-j] == 'H' and check_list[i-j] == 0: # 사람 기준 왼쪽 먼저 탐색
                
#                 # print('j: ', j)
#                 cnt += 1
#                 check_list[i-j] = 1
#                 # print("c_l - : ", i-j)
#                 break # 햄버거 먹으면 해당 반복문(j) 빠져나옴
#             elif i+j < len(seq) and seq[i+j] == 'H' and check_list[i+j] == 0: # 왼쪽에 햄버거가 없을 경우 오른쪽 탐색
#                 # print('j: ', j)
#                 cnt += 1
#                 check_list[i+j] = 1
#                 # print("c_l + : ", i+j)
#                 break # 햄버거 먹으면 해당 반복문(j) 빠져나옴

# print(cnt)