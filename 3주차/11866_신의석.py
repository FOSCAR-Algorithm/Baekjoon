N, K = map(int,input().split())
temp = K-1
Circlist = []


for i in range(1,N+1):
    Circlist.append(i)
print("<", end = '')

while len(Circlist)> 1:
    if temp>=len(Circlist):
        temp = temp - len(Circlist)
    else:
        print(Circlist.pop(temp), end = ", ")
        temp += K-1

print(f"{Circlist[0]}>")
