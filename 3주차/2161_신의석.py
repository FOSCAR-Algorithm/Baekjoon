N = int(input())
Clist = []
for i in range(1,N+1):
    Clist.append(i)

while len(Clist)>=2:
    print(Clist.pop(0),end=' ')
    Clist.append(Clist.pop(0))
print(Clist[0])

