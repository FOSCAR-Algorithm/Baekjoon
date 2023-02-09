N = int(input())
tList = list(map(int,input().split()))
ans = 0
tList.sort()
tList.reverse()
ans = 2

for i in range(N):
    tList[i] += i
ans = max(tList)

print(ans)










