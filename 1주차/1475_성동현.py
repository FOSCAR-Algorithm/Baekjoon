def plasticset(n):
    num_str=list(str(num)) #자리마다 숫자를 비교하기 위해 문자열로 바꾼 후 리스트로 저장한다.
    min=1 #필요한 최소개수를 저장하는 변수를 설정한다.
    num2=0 #6과 9를 따로 저장할 변수를 설정한다.
    for i in range(0, len(num_str)): # 개수를 센 숫자를 표시하기 위해 -1이라는 숫자를 원래 숫자 대신 저장한다.
        imin=1
        if num_str[i]!='-1': #
            if num_str[i] != '6' and num_str[i] != '9': #6과 9는 놔둔채로 나머지 숫자만 비교한다.
                for z in range(i+1,len(num_str)):
                        if num_str[i]==num_str[z]:
                            imin+=1
                            num_str[z]='-1'
        if imin > min: #각 숫자들의 개수가 이전까지 셌던 최소 개수보다 많을 시 그 개수를 대체한다.
            min = imin

    for i in range(0, len(num_str)): #남아있는 6과 9를 한꺼번에 계산한다.
        if num_str[i]=='6' or num_str[i]=='9':
            num2+=1

    if (num2+1)//2>min: # 마지막으로 최소개수와 6과9의 개수를 비교한 후 최종적으로 개수를 결정한다,
        min=(num2+1)//2
    print(min) #최소개수를 표시한다.



if __name__ =="__main__":
    num=int(input())
    plasticset(num)