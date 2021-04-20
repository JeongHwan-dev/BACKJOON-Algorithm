"""
예제 입력 1
5
5
4
3
2
1

예제 출력 1
1
2
3
4
5
"""

import sys

n = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
num_list.sort()

for num in num_list:
    print(num)
