def control_radio(A,B,N): # 3개의 파라미터를 입력받는 주파수 조절 함수
    hz_List=[] # 라디오 주파수를 저장할 리스트 선언
    hz_List.append(A)

    for _ in range(N): # 미리 지정되어 있는 주파수를 저장하는 반복문
        list_hz=int(input())
        hz_List.append(list_hz)

    for i in range(len(hz_List)): # 주파수값을 간격(버튼 수)으로 대체하는 반복문
        interval=B-hz_List[i]
        if interval<0: # 음수가 나올 경우
            hz_List[i]=-interval
        else: # 양수가 나올 경우
            hz_List[i]=interval
        if i>0: # i가 0일떄를 제외하고는 지정되어있는 주파수를 불러오기위한 버튼을 1번 눌러야 함을 고려한 조건문
            hz_List[i]+=1 # 간격(버튼 수)에 버튼 수 1을 추가하는 코드

    return min(hz_List) # min함수를 통해 가장 작은 버튼 수를 리턴한다.


if __name__=="__main__":
    A,B=map(int , input().split())
    N=int(input())
    print(control_radio(A,B,N))

    # list=["A","지정된 주파수 1","지정된 주파수 2","지정된 주파수 3","........."]
    # aList=["interval (1)","interval (2)","interval (3)","interval (4)"]
    # print(list)
    # print(aList)