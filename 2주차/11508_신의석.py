N = int(input())
CList = []
for i in range(N):
    C=int(input())
    CList.append(C)

CList.sort(reverse=True)
i=2
ans = 0
while i<=N-1:
    CList[i]=0
    i+=3

print(sum(CList))