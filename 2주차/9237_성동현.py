def shell_sort(sList):
    n=len(sList)
    h=n//2
    while h>0:
        for start in range(0,h):
            for end in range(h,n,h):
                for i in range(end,0,-h):
                    if sList[i - 1] < sList[i]:
                        sList[i - 1], sList[i] = sList[i], sList[i - 1]
        h//=2
def insertion_sort(sList):
    n=len(sList)
    for end in range(1,n):
        for i in range(end,0,-1):
            if sList[i - 1] < sList[i]:
                sList[i - 1], sList[i] = sList[i], sList[i - 1]

def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr





def count_tree():
    tree_time=list(map(int, input().split()))
    tree_time.sort(reverse=True) #내림차 순 정리
    total=0
    current=1 #시작일을 1일으로 설정
    for i in range(0,len(tree_time)):
        if current+tree_time[i]+1>total:
            total=current+tree_time[i]+1 #해당 숫자로 대체
        current+=1
    return total



if __name__=="__main__":
    N=int(input())
    print(count_tree())