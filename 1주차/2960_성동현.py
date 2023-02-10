
def search_num(num,k):
    aList = [i for i in range(2, num + 1)] #리스트 안 반복문을 통해 숫자를 세팅한다.
    num2=0
    cnt=0 #원하는 카운트에 맞는 숫자를 고르기 위해 카운트 값을 저장할 변수
    for i in range(len(aList)):
        if aList[i]!=0:
            mut=num//aList[i] # 해당 소수의 배수가 몇까지 존재하는지 알아보기 위한 변수
            temp=aList[i] # 배수를 곱할 소수를 저장하는 변수
            for z in range(1,mut+1):
                if aList[temp*z-2]!=0:
                    cnt += 1
                    print(f"cnt값은 {cnt}")
                    base=aList[temp*z-2] #temp*z-2인 이유는 숫자가 2부터 시작하기 때문에 인덱스 설정 상 해당 숫자 곱하기 배수-2가 인덱스 값이 된다.
                    if cnt==k:
                        num2+=base
                        break
                    aList[temp*z-2]=0 #지워진 숫자를 알아보기 위해 원래 값 대신 0을 저장한다.
                    print(aList)
        else:
            pass
        if cnt==k:
            break
    return num2





if __name__ =="__main__":
    num, k= map(int,input().split())
    print(search_num(num,k))
