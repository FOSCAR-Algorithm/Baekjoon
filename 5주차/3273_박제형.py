# 두 수의 합
# https://www.acmicpc.net/problem/3273

# set에서 in 연산자 : O(1) / list에서 in 연산자 : O(N) => 시간복잡도 위해 set 사용
# set는 hash 통해서 자료들을 저장하기 때문에 O(1) / list는 하나하나 순회 O(N)
n = int(input())

num_list = set(sorted(list(map(int, input().split()))))


x = int(input())

cnt = 0

for i in num_list:
    if x-i in num_list:
        cnt += 1

# for i in range(n):
#     for j in range(n-1, i, -1):
#         print(num_list[i], num_list[j])
#         if i == j:
#             break
#         if num_list[i] + num_list[j] == x:
#             cnt += 1
#             break

print(int(cnt/2))