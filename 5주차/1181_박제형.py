# 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys

n = int(sys.stdin.readline())

temp_list = []

for i in range(n):
    temp_list.append(sys.stdin.readline().strip())

temp_list = list(set(temp_list))
# temp_list = list(temp_set)

# 단어 길이, 단어를 같이 담을 list 선언
string_list =  []


for i in range(len(temp_list)):
    # 단어 길이, 단어 append
    string_list.append((len(temp_list[i]), temp_list[i]))

sorted_list = sorted(string_list)

for len, word in sorted_list:
    print(word)