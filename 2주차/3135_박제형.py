# 라디오
# https://www.acmicpc.net/problem/3135

a, b = map(int, input().split())
N = int(input())
favorite = [] # 즐겨찾기 목록 list

for i in range(N): # 즐겨찾기 입력
    favorite.append(int(input()))

min = abs(a-b) 

click=0
for x in favorite: # 즐겨찾기 목록 탐색하면서 a-b 보다 차가 적으면 min update
    if min > abs(x-b):
        min = abs(x-b)

if min != abs(a-b): # min이 update 되었으면(즐겨찾기 내 채널이 a-b보다 작으면) click++
    click+=1

if min>0: # 남은 차 만큼 click ++ 
    click+=min

print(click)