# 별찍기
# https://www.acmicpc.net/problem/10994

def draw(n, idx):
    if n == 1:
        star[idx][idx] = '*'
        return # n == 1이 될 때 return 하며 재귀 종료
    
    l = 4 * n - 3
    # N=2일때 l=5 / N=3일때 l=9
    for i in range(idx, idx+l): # l 크기 만큼 테두리를 * 로 
        # 맨 위, 맨 아래
        star[idx][i] = '*'
        star[idx+l-1][i] = '*'

        # 양 옆 열
        star[i][idx] = '*'
        star[i][idx+l-1] = '*'

    return draw(n-1, idx+2) # n=2 의 그림이 n=3 그림에서 행, 열을 2칸씩 이동해서 그리는 것이므로 idx+2

N = int(input())
num = 4 * N - 3
star = [[' '] * num for _ in range(num)] # 빈칸으로 채워져있는 num*num 크기의 2차원 배열

# N부터 (4N-3)크기의 큰 바깥 테두리를 그리면서 N-1를 재귀함수로 호출하면서 작은 네모를 그려감
draw(N, 0)

# print(*star)
for i in range(num):
    for j in range(num):
        print(star[i][j], end='')
    print()