"""
예제 입력 1
10
5
2
3
1
4
2
3
5
1
7

예제 출력 1
1
1
2
2
3
3
4
5
5
"""

import sys

N = int(input())
check_list = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    check_list[num] = check_list[num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)
