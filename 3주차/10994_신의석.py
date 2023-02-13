def Star(num, index):
    if num == 1:
        arr[index][index] = '*'
        return
    unit = 4 * num -3

    for i in range(index,index+unit):
        arr[index][i] = '*'
        arr[index+unit-1][i] = '*'

        arr[i][index] = '*'
        arr[i][index + unit - 1] = '*'

    return Star(num-1, index +2)





if __name__ == "__main__":
    N = int(input())
    arr = [[' '] * (4*N-3) for i in range(4*N-3)]
    Star(N,0)

    for i in range(4 * N - 3):
        for j in range(4 * N - 3):
            print(arr[i][j], end='')
        print()
