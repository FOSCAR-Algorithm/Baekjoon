from itertools import combinations

def suggetion(tList):
    for i in range(len(tList)):
        s = list(combinations(tList[i],6))
        for j in s:
            for k in j:
                print(k,end= ' ')
            print()
        print()

if __name__ == '__main__':
    temp = []

    while True:
        lotto_num = list(map(int, input().split()))
        if 0 == lotto_num[0]:
            break
        lotto_num.pop(0)

        temp.append(lotto_num)
    suggetion(temp)










