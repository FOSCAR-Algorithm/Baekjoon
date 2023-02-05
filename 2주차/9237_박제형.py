# 이장님 초대
# https://www.acmicpc.net/problem/9237

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True) # 리스트 t 내림차순 정렬

max =  t[0] + 1 # 가장 오래 걸리는 나무가 완전히 자라는 날짜를 기준으로 max 설정

# i(심는 날짜) + t[i](걸리는 시간) + 1(심는 데 하루 걸림) 계산을 통해서 각 나무별 완전히 자라는 날짜 파악
for i in range(1, len(t)): # 모든 나무를 탐색하며 max값보다 늦게 자라는 나무가 있을 경우 max 변경
    if max < i + t[i] + 1:
        max = i + t[i] + 1

print(max+1) # 이장님은 나무가 완전히 자란 다음날에 부르므로 +1