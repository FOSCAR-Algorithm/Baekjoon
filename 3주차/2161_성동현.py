def shake_card(N):
    queue=[i for i in range(1,N+1)]
    gabage_list=[]
    for _ in range(N-1):
        gabage_list.append(queue.pop(0))
        queue.append(queue.pop(0))
    gabage_list.append(queue.pop())
    for i in range(0,len(gabage_list)):
        print(gabage_list[i],end=' ')


if __name__=="__main__":
    shake_card(int(input()))
