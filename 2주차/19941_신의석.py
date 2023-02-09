N, K = map(int, input().split())

HPlist = list(input())
ans = 0

#최대한 왼쪽 햄버거 먹기
for i in range(N):# 이미 먹힌 햄버거는 Eaten
    if HPlist[i]=="P":
        for j in range(max(0,i-K),min(N,i+K+1)):
            if HPlist[j]=='H':
                HPlist[j]='E'
                ans+=1
                break

print(ans)