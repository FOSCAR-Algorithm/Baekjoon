# 나이트의 이동
# https://www.acmicpc.net/problem/7562

# bfs, queue 이용

from collections import deque

# 한 지점에서 방문할 수 있는 모든 경우의 수
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(sx, sy, tx, ty):
    queue = deque()
    queue.append([sx, sy])
    chess[sx][sy] = 0 # 시작점 (0) 으로 세팅

    while queue:
        a, b = queue.popleft()

        if a == tx and b == ty: # 시작점 = 목표점(종료 조건)
            print(chess[tx][ty]) 
            return
        for i in range(8): # 한 점에서 가능한 모든 곳 방문
            x = a + dx[i]
            y = b + dy[i]
            # chess 칸의 범위에 벗어나지 않고 방문하지 않은 곳이면
            if 0 <= x < I and  0 <= y < I and chess[x][y] == 0:
                queue.append([x, y])
                chess[x][y] = chess[a][b] + 1 # 직전 값 + 1


# 입력
tc = int(input())
for i in range(tc):
    # 체스판의 크기
    I = int(input()) 

    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    # 입력받은 크기에 맞는 체스판 만들기
    chess = [[0] * I for _ in range(I)]

    bfs(start_x, start_y, target_x, target_y)