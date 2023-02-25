# 30
# https://www.acmicpc.net/problem/10610

# 30의 배수가 되는 가장 큰 수

num = list(input())

sum = 0
for i in num:
    sum += int(i)

# 조건 : 0 포함, 모든 자리를 더했을 때 3으로 나눠떨어져야함 -> 조건에 부함X => -1 출력
if '0' not in num or sum % 3 != 0:
    print("-1")
else:
    num.sort(reverse=True)
    print(''.join(num))