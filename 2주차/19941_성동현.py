def devide_burger():
    N,K=map(int,input().split())
    sList=list(input())
    table=['0' for i in range(K)]+sList+['0' for i in range(K)] #앞뒤로 0을 K개수 만큼 채운 리스트(코드를 효율적으로 짜기 위한 방법)
    cnt=0
    for i in range(K,len(table)):
        if table[i]=='P':
            for k in range(i-K, i+K+1): # i-k가 절대 음수가 나오지 않도록 위에 짠 코드를 기반으로 반복문을 시도한다.
                if table[k] == 'H':
                        table[k] = '0'
                        cnt += 1
                        break
    print(cnt)

if __name__=="__main__":
    devide_burger()


