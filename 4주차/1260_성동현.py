from collections import deque


def Graph():
    N,M,v=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    dfs_list=[]
    bfs_list=[]
    visited=['False']*(N+1)

    for i in range(M):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(len(graph)):
        graph[i].sort()



    def dfs(graph, v, visited):
        visited[v]='True'
        dfs_list.append(v) #정점을 저장하는 리스트

        for i in graph[v]:
            if visited[i]=='False':
                dfs(graph,i,visited)

    def bfs(graph, start, visited):
        queue=deque([start])
        visited[start]='False'
        while queue:
            v=queue.popleft()
            bfs_list.append(v) #정점을 저장하는 리스트

            for i in graph[v]:
                if visited[i]=='True':
                    queue.append(i)
                    visited[i]='False'

    dfs(graph, v, visited)
    bfs(graph, v, visited)
    print(*dfs_list)
    print(*bfs_list)


if __name__=="__main__":
    Graph()