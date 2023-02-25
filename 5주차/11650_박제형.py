# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

n = int(sys.stdin.readline())

sort_list = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    sort_list.append([x, y])

sort_list.sort()

for x, y in sort_list:
    print(x, y)