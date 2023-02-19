# import sys
# sys.setrecursionlimit(10**7)
#
#
# def number():
#     number_list=[]
#     for _ in range(5):
#         aList=list(map(int, sys.stdin.readline().split()))
#         number_list.append((aList))
#     case_list=[]
#     direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#
#     def fine_case(a,b):
#         case=[]
#         def dfs(x,y,depth):
#             if x<=-1 or x>=5 or y<= -1 or y>=5:
#                 case.pop()
#                 return
#             else:
#                 case.append(number_list[x][y])
#                 if depth==6: #재귀함수 종료조건
#                     cnt=0
#                     for i in range(len(case_list)):
#                         for z in range(6):
#                             if case_list[i][z] == case[z]:
#                                 cnt+=1
#                     if cnt!=6:
#                         case_list.append(case)
#                         case.clear()
#
#                     return
#                 for i_x,i_y in direction:
#                     dfs(x+i_x,y+i_y,depth+1)
#         dfs(a,b,1)
#         print(case)
#
#     for i in range(5):
#         for z in range(5):
#             fine_case(i,z)
#     print(len(case_list))
#
#
# if __name__=="__main__":
#     number()


def dfs(x, y, number):
    if len(number) == 6:  # 6자리 숫자가 만들어졌다면
        if number not in result:  # result에 없다면
            result.append(number)
        return

    dx = [1, -1, 0, 0]  # 상하좌우 확인 x
    dy = [0, 0, 1, -1]  # 상하좌우 확인 y
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]

        if 0 <= ddx < 5 and 0 <= ddy < 5:  # 범위 내에 있다면
            dfs(ddx, ddy, number + matrix[ddx][ddy])  # 6글자가 될 때 까지 재귀


# 입력
matrix = [list(map(str, input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])  # 0,0부터 4,4까지 모두 검사
print(len(result))











