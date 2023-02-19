from collections import deque
def Night():
    n=int(input())
    x,y=map(int,input().split())
    r_x,r_y=map(int,input().split())
    direction=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]] #방향 설정
    graph=[[0 for _ in range(n)] for _ in range(n)] #shallow cop
    #graph=[[0]*n]*n


    def bfs(x,y):
        if x==r_x and y==r_y:
            print(0)
            return
        queue=deque()
        queue.append([x,y])

        while graph[r_x][r_y]==0: #경로가 탐색될 시  while문을 벗어남으롯써 함수를 끝내게 된다.
            x,y=queue.popleft()
            for x_i,y_i in direction:
                nx= x+x_i
                ny= y+y_i

                if nx<0 or nx>=n or ny <0 or ny >=n:
                    continue

                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append([nx,ny])

        print(graph[r_x][r_y])

    bfs(x,y)

if __name__ =="__main__":
    cnt=int(input())
    for _ in range(cnt):
        Night()