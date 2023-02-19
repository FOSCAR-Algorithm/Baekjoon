# 숫자판 점프
# https://www.acmicpc.net/problem/2210

import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 4 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, num):
    num += grid[x][y] # recursion error -> set해주면 메모리초과 why??

    if len(num) == 6: # 재귀함수 종료 조건
        result.add(num)
        return
    
    # 4 방향 탐색
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if 0 <= temp_x < 5 and 0 <= temp_y < 5: # grid 내로 범위 제한
            dfs(temp_x, temp_y, num) # len(num) == 6 까지 dfs, 여기서 num에 다음 grid 숫자 더해줌



# 숫자판 입력 (5줄의 str 값 5개 list)
grid = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]

result = set() # 중복 제거 위해 set 사용

# (0,0) ~ (4,4) 까지 모든 점에서 dfs 
for i in range(5):
    for j in range(5):
        dfs(i, j, grid[i][j]) # gird[i][j]를 num으로 보내면서 dfs 통해서 num을 쌓아감 

print(len(result))