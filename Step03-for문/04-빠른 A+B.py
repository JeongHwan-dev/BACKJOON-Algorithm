"""
예제 입력 1
5
1 1
12 34
5 500
40 60
1000 1000

예제 출력 1
2
46
505
100
2000
"""

import sys

n = int(input())
result = []

for i in range(n):
    num1, num2 = map(int, sys.stdin.readline().split())
    result.append(num1 + num2)

for r in result:
    print(r)
