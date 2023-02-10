def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


def count_price(N):
    sList=[]
    for _ in range(N):
        sList.append(int(input()))
    price_list=merge_sort(sList)
    total=sum(price_list)
    for i in range(2,len(price_list),3):
        total-=price_list[i]
    return total




if __name__=="__main__":
    N=int(input())
    print(count_price(N))
