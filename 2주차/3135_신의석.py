A, B = map(int, input().split())
N = int(input())
HzList = [] # 주파수 리스트
for i in range(N):# 즐겨찾기 주파수 리스트
    hz = int(input())
    HzList.append(hz)
ans = 1000

for i in range(N):#즐겨찾기 주파수 리스트와 비교하기
    if B==HzList[i]:
        ans = min(1,ans)
    elif abs(A-B)>abs(HzList[i]-B)+1:
        ans = min(abs(HzList[i]-B)+1,ans)
    else:
        ans = min(abs(A-B),ans)

print(ans)