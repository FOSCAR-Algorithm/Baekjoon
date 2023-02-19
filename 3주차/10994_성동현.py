def Total_star(N):
    list=[[" "for _ in range(4*N-3)] for _ in range(4*N-3)]

    def star_maker(n, x, y):
        if n==1:
            list[y][x]="*"
            return
        l=4*n-3

        for i in range(l):
            list[y][x+i]="*"
            list[y+i][x]="*"
            list[y+l-1][x+i]="*"
            list[y+i][x+l-1]="*"
        star_maker(n-1,x+2,y+2)
    star_maker(N,0,0)
    for i in list:
        print("".join(i))




if __name__=="__main__":
    Total_star(int(input()))









