def Josephus():
    N,K=map(int, input().split())
    queue=[i for i in range(1,N+1)]
    gabage_list=[]
    for _ in range(N):
        for i in range(K-1):
            queue.append(queue.pop(0))
        gabage_list.append(queue.pop(0))
    print("<",end="")
    for i in range(len(gabage_list)-1):
        print(f"{gabage_list[i]},", end=" ")
    print(f"{gabage_list[len(gabage_list)-1]}>")

if __name__=="__main__":
    Josephus()
