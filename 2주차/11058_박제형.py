# 2+1 세일
# https://www.acmicpc.net/problem/11508

n = int(input())
cost = []

# 각 유제품 별 값 입력받음
for i in range(n):
    cost.append(int(input()))

# 값 내림차순 정렬 (내림차순으로 정렬하여 3개씩 묶어야 가장 저렴하게 구매할 수 있음)
cost.sort(reverse=True)

result = 0

# cost를 내림차순한 값들 중 3의 배수 번째를 제외하고 result에 더함
for i in range(n):
    if i > 0 and (i+1) % 3 == 0:
        continue
    result += cost[i]

print(result)