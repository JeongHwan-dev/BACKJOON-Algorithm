"""
예제 입력 1
5
2 4 -10 4 -9
예제 출력 1
2 3 0 3 1

예제 입력 2
6
1000 999 1000 999 1000 999
예제 출력 2
1 0 1 0 1 0
"""

import sys
input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))
sorted_x_list = list(sorted(set(x_list)))
x_dic = {value: index for index, value in enumerate(sorted_x_list)}

for x in x_list:
    print(x_dic[x], end=' ')
