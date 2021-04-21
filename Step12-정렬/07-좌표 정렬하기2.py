"""
예제 입력 1
5
0 4
1 2
1 -1
2 2
3 3

예제 출력 1
1 -1
1 2
2 2
3 3
0 4
"""

import sys

n = int(sys.stdin.readline())
coordinate = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([x, y])

coordinate.sort(key=lambda c: (c[1], c[0]))

for x, y in coordinate:
    print(x, y)
