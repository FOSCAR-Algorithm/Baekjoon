def lotto(aList):
    aList.pop(0)
    lotto_part = [0 for _ in range(6)]

    def dfs(start,depth):

        if depth==6:
            print(*lotto_part)
            return

        for i in range(start,len(aList)):
            lotto_part[depth]=aList[i]
            dfs(i+1,depth+1)
    dfs(0,0)




if __name__=="__main__":
    while 1:
        aList=list(map(int, input().split()))
        if aList[0]==0:
            break
        lotto(aList)
        print("")
